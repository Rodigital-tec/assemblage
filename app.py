import os
import sys
import hashlib
from datetime import timedelta
from dotenv import load_dotenv

from flask import Flask, send_from_directory, request, jsonify, session, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_cors import CORS

# Charger les variables d'environnement
load_dotenv()

# Import des modèles
from models import db, User, SMTPConfig, HelpRequest
from routes.auth_simple import auth_bp
from routes.auth_working import auth_working_bp
from routes.service_types import service_types_bp
from routes.help_requests import help_requests_bp
from routes.help_requests_simple import help_requests_simple_bp
from routes.service_offers import service_offers_bp
from routes.user_profile import user_profile_bp
from routes.user_profile_api import user_profile_bp as user_profile_api_bp
from routes.messages import messages_bp
from routes.admin_api import admin_api_bp
from routes.init_db import init_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configuration de l'environnement
is_production = os.getenv('FLASK_ENV') == 'production'

# Configuration de la clé secrète
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'assemblage_secret_key_2024_secure')
app.config['SESSION_COOKIE_SECURE'] = is_production  # HTTPS en production
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Configuration CORS
CORS(app, supports_credentials=True, origins=['*'])

# Configuration de la base de données
database_url = os.getenv('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration des uploads
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialisation des extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
login_manager.session_protection = "strong"
login_manager.remember_cookie_duration = timedelta(days=7)

def hash_password(password):
    """Simple password hashing using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, hashed):
    """Check password against hash - compatible avec les comptes de test"""
    # Pour les comptes de test, vérifier d'abord si c'est un mot de passe en texte brut
    if password == hashed:
        return True
    # Sinon, vérifier avec le hachage SHA-256
    return hashlib.sha256(password.encode()).hexdigest() == hashed

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes d'authentification simplifiées
@app.route('/login-simple', methods=['POST'])
def login_simple():
    """Route de connexion simple depuis le formulaire HTML"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and check_password(password, user.password_hash):
        login_user(user, remember=request.form.get('remember', False))
        
        # Ajouter les informations à la session
        session['user_id'] = user.id
        session['user_email'] = user.email
        session['user_type'] = user.user_type
        
        # Redirection selon le type d'utilisateur
        if user.user_type == 'admin':
            return redirect('/admin.html')
        else:
            return redirect('/dashboard.html')
    else:
        return redirect('/?error=invalid_credentials')

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and check_password(password, user.password_hash):
        login_user(user, remember=data.get('remember', False))
        
        # Ajouter l'ID utilisateur à la session pour l'API alternative
        session['user_id'] = user.id
        session['user_email'] = user.email  # Ajouter l'email pour l'API profil
        
        # Retourner les informations utilisateur pour la redirection
        return jsonify({
            'success': True, 
            'redirect': '/admin.html' if user.user_type == 'admin' else '/dashboard.html',
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_type': user.user_type
            }
        })
    else:
        return jsonify({'success': False, 'error': 'Email ou mot de passe incorrect'}), 401

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True})

@app.route('/api/auth/check-auth')
def check_auth():
    if current_user.is_authenticated:
        return jsonify({
            'authenticated': True,
            'user': {
                'id': current_user.id,
                'email': current_user.email,
                'first_name': current_user.first_name,
                'last_name': current_user.last_name,
                'user_type': current_user.user_type
            }
        })
    return jsonify({'authenticated': False})

@app.route('/api/admin/stats')
@login_required
def admin_stats():
    if current_user.user_type != 'admin':
        return jsonify({'error': 'Accès non autorisé'}), 403
    
    total_users = User.query.count()
    return jsonify({
        'total_users': total_users,
        'active_requests': 0,
        'total_messages': 0,
        'pending_moderation': 0
    })

@app.route('/api/admin/users')
@login_required
def admin_users():
    if current_user.user_type != 'admin':
        return jsonify({'error': 'Accès non autorisé'}), 403
    
    users = User.query.all()
    users_data = []
    
    for user in users:
        users_data.append({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'user_type': user.user_type,
            'is_active': user.is_active,
            'created_at': user.created_at.isoformat() if user.created_at else None
        })
    
    return jsonify({
        'users': users_data,
        'pagination': {
            'page': 1,
            'pages': 1,
            'total': len(users_data)
        }
    })

# Création des tables
with app.app_context():
    # Créer le dossier uploads s'il n'existe pas
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Créer toutes les tables
    db.create_all()
    
    # Créer un utilisateur admin par défaut s'il n'existe pas
    admin_user = User.query.filter_by(email='admin@assemblage.ch').first()
    if not admin_user:
        admin_user = User(
            email='admin@assemblage.ch',
            password_hash=hash_password('admin123'),
            first_name='Admin',
            last_name='Assemblage',
            user_type='admin',
            is_active=True,
            email_verified=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Utilisateur admin créé: admin@assemblage.ch / admin123")
    
    # Charger la configuration SMTP
    try:
        smtp_config = SMTPConfig.query.first()
        if smtp_config:
            app.config['MAIL_SERVER'] = smtp_config.smtp_server
            app.config['MAIL_PORT'] = smtp_config.smtp_port
            app.config['MAIL_USERNAME'] = smtp_config.smtp_username
            app.config['MAIL_PASSWORD'] = smtp_config.smtp_password
            app.config['MAIL_USE_TLS'] = smtp_config.use_tls
            app.config['MAIL_USE_SSL'] = False
            print("Configuration SMTP chargée")
    except Exception as e:
        print(f"Erreur lors du chargement de la configuration SMTP: {e}")

@app.route('/api/current-user-simple')
def get_current_user_simple():
    """API simplifiée pour récupérer l'utilisateur connecté"""
    try:
        # Essayer d'abord avec Flask-Login
        if current_user.is_authenticated:
            user_data = {
                'id': current_user.id,
                'email': current_user.email,
                'first_name': current_user.first_name,
                'last_name': current_user.last_name,
                'user_type': current_user.user_type,
                'phone': getattr(current_user, 'phone', ''),
                'city': getattr(current_user, 'city', ''),
                'is_active': current_user.is_active
            }
            return jsonify({'success': True, 'user': user_data})
        
        # Sinon essayer avec la session
        elif 'user_email' in session:
            user = User.query.filter_by(email=session['user_email']).first()
            if user:
                user_data = {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'user_type': user.user_type,
                    'phone': getattr(user, 'phone', ''),
                    'city': getattr(user, 'city', ''),
                    'is_active': user.is_active
                }
                return jsonify({'success': True, 'user': user_data})
        
        return jsonify({'success': False, 'message': 'Non authentifié'}), 401
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/current-user')
@login_required
def get_current_user():
    """Récupère les informations de l'utilisateur connecté"""
    try:
        user_data = {
            'id': current_user.id,
            'email': current_user.email,
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'user_type': current_user.user_type,
            'phone': getattr(current_user, 'phone', ''),
            'city': getattr(current_user, 'city', ''),
            'is_active': current_user.is_active
        }
        return jsonify({'success': True, 'user': user_data})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

# Route profil simple qui fonctionne toujours
@app.route('/profile-data')
def get_profile_data():
    """Route simple pour récupérer les données de profil sans authentification complexe"""
    # Pour le moment, retourner les données de test
    profiles = {
        'marie.dupont@email.com': {
            'first_name': 'Marie',
            'last_name': 'Dupont', 
            'email': 'marie.dupont@email.com',
            'phone': '+41 22 234 56 78',
            'address': '15 Rue du Lac',
            'biography': 'Retraitée active, j\'aime la lecture et les promenades.',
            'user_type': 'senior',
            'has_driving_license': False,
            'created_at': '2025-09-08',
            'stats': {'help_requests': 5, 'messages': 0}
        },
        'sophie.leroy@email.com': {
            'first_name': 'Sophie',
            'last_name': 'Leroy',
            'email': 'sophie.leroy@email.com', 
            'phone': '+41 22 456 78 90',
            'address': '22 Chemin des Fleurs',
            'biography': 'Infirmière à temps partiel, disponible pour aider les seniors.',
            'user_type': 'aidant',
            'has_driving_license': True,
            'created_at': '2025-09-08',
            'stats': {'offers': 3, 'messages': 0}
        },
        'admin@assemblage.ch': {
            'first_name': 'Admin',
            'last_name': 'Assemblage',
            'email': 'admin@assemblage.ch',
            'phone': '+41 22 000 00 00', 
            'address': 'Lausanne, Suisse',
            'biography': 'Administrateur de la plateforme Assembl\'âge.',
            'user_type': 'admin',
            'has_driving_license': True,
            'created_at': '2025-09-08',
            'stats': {'users': 8, 'requests': 15}
        }
    }
    
    email = request.args.get('email', 'marie.dupont@email.com')
    profile = profiles.get(email, profiles['marie.dupont@email.com'])
    
    return jsonify({
        'success': True,
        'user': profile,
        'stats': profile['stats']
    })
@app.route('/api/profile/<email>')
def get_profile_by_email(email):
    """API pour récupérer le profil par email"""
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'success': False, 'error': 'Utilisateur non trouvé'}), 404
        
        # Statistiques de l'utilisateur
        stats = {}
        
        if user.user_type == 'senior':
            help_requests_count = HelpRequest.query.filter_by(senior_id=user.id).count()
            stats = {
                'help_requests': help_requests_count,
                'messages': 0,
                'availability': 'Actif'
            }
        else:  # aidant
            service_offers_count = 0  # À implémenter si nécessaire
            stats = {
                'service_offers': service_offers_count,
                'messages': 0,
                'availability': 'Disponible'
            }
        
        return jsonify({
            'success': True,
            'profile': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone': user.phone or '',
                'address': user.address or '',
                'bio': user.biography or '',
                'user_type': user.user_type,
                'has_driving_license': getattr(user, 'has_driving_license', False),
                'created_at': user.created_at.isoformat() if user.created_at else '',
                'stats': stats
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# API pour mettre à jour le profil par email
@app.route('/api/profile/<email>', methods=['PUT'])
def update_profile_by_email(email):
    """API pour mettre à jour le profil par email"""
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'success': False, 'error': 'Utilisateur non trouvé'}), 404
        
        data = request.get_json()
        
        # Mise à jour des champs
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'phone' in data:
            user.phone = data['phone']
        if 'address' in data:
            user.address = data['address']
        if 'bio' in data:
            user.biography = data['bio']
        if 'has_driving_license' in data:
            user.has_driving_license = data['has_driving_license']
        
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Profil mis à jour avec succès'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

# Enregistrement des blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(auth_working_bp)
app.register_blueprint(service_types_bp)
app.register_blueprint(help_requests_bp)
app.register_blueprint(help_requests_simple_bp)
app.register_blueprint(service_offers_bp)
app.register_blueprint(user_profile_bp)
app.register_blueprint(user_profile_api_bp)
app.register_blueprint(messages_bp)
app.register_blueprint(admin_api_bp)
app.register_blueprint(init_bp)

# Import et enregistrement du nouveau blueprint profile_api
try:
    from routes.profile_api import profile_api
    app.register_blueprint(profile_api)
except ImportError:
    pass

# Import et enregistrement de l'API de recherche géolocalisée
try:
    from routes.search_api import search_api
    app.register_blueprint(search_api)
except ImportError:
    pass

# Import et enregistrement de l'API des statistiques
try:
    from routes.stats_api import stats_bp
    app.register_blueprint(stats_bp)
except ImportError:
    pass

# Import et enregistrement de l'API des notifications
try:
    from routes.notifications_api import notifications_bp
    app.register_blueprint(notifications_bp)
except ImportError:
    pass

# Import et enregistrement des APIs d'administration
try:
    from routes.admin_auth import admin_auth_bp
    from routes.admin_users import admin_users_bp
    from routes.admin_moderation import admin_moderation_bp
    from routes.admin_config import admin_config_bp
    from routes.admin_analytics import admin_analytics_bp

    app.register_blueprint(admin_auth_bp, url_prefix='/api/admin/auth')
    app.register_blueprint(admin_users_bp, url_prefix='/api/admin')
    app.register_blueprint(admin_moderation_bp, url_prefix='/api/admin/moderation')
    app.register_blueprint(admin_config_bp, url_prefix='/api/admin')
    app.register_blueprint(admin_analytics_bp, url_prefix='/api/admin/analytics')
except ImportError as e:
    print(f"Modules d'administration non disponibles: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

