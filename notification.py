from datetime import datetime
from models import db

class Notification(db.Model):
    """Modèle pour les notifications utilisateur"""
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'message', 'request', 'appointment', 'opportunity'
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text)
    data = db.Column(db.JSON)  # Données additionnelles (IDs, URLs, etc.)
    read_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relation avec l'utilisateur
    user = db.relationship('User', backref=db.backref('notifications', lazy=True))
    
    def __repr__(self):
        return f'<Notification {self.id}: {self.title}>'
    
    def to_dict(self):
        """Convertir la notification en dictionnaire"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'type': self.type,
            'title': self.title,
            'message': self.message,
            'data': self.data,
            'read_at': self.read_at.isoformat() if self.read_at else None,
            'created_at': self.created_at.isoformat(),
            'is_read': self.read_at is not None
        }
    
    def mark_as_read(self):
        """Marquer la notification comme lue"""
        self.read_at = datetime.utcnow()
        db.session.commit()
    
    @staticmethod
    def create_notification(user_id, notification_type, title, message=None, data=None):
        """Créer une nouvelle notification"""
        notification = Notification(
            user_id=user_id,
            type=notification_type,
            title=title,
            message=message,
            data=data
        )
        db.session.add(notification)
        db.session.commit()
        return notification
    
    @staticmethod
    def get_user_notifications(user_id, limit=20, unread_only=False):
        """Récupérer les notifications d'un utilisateur"""
        query = Notification.query.filter_by(user_id=user_id)
        
        if unread_only:
            query = query.filter(Notification.read_at.is_(None))
        
        return query.order_by(Notification.created_at.desc()).limit(limit).all()
    
    @staticmethod
    def count_unread(user_id):
        """Compter les notifications non lues d'un utilisateur"""
        return Notification.query.filter_by(user_id=user_id).filter(Notification.read_at.is_(None)).count()
    
    @staticmethod
    def mark_all_as_read(user_id):
        """Marquer toutes les notifications d'un utilisateur comme lues"""
        notifications = Notification.query.filter_by(user_id=user_id).filter(Notification.read_at.is_(None)).all()
        for notification in notifications:
            notification.read_at = datetime.utcnow()
        db.session.commit()
        return len(notifications)


class Appointment(db.Model):
    """Modèle pour les rendez-vous"""
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    aidant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    senior_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    help_request_id = db.Column(db.Integer, db.ForeignKey('help_requests.id'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('planned', 'confirmed', 'completed', 'cancelled', name='appointment_status'), default='planned')
    location = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relations
    aidant = db.relationship('User', foreign_keys=[aidant_id], backref='appointments_as_aidant')
    senior = db.relationship('User', foreign_keys=[senior_id], backref='appointments_as_senior')
    help_request = db.relationship('HelpRequest', backref='appointments')
    
    def __repr__(self):
        return f'<Appointment {self.id}: {self.title}>'
    
    def to_dict(self):
        """Convertir le rendez-vous en dictionnaire"""
        return {
            'id': self.id,
            'aidant_id': self.aidant_id,
            'senior_id': self.senior_id,
            'help_request_id': self.help_request_id,
            'title': self.title,
            'description': self.description,
            'start_datetime': self.start_datetime.isoformat(),
            'end_datetime': self.end_datetime.isoformat(),
            'status': self.status,
            'location': self.location,
            'created_at': self.created_at.isoformat(),
            'aidant_name': f"{self.aidant.first_name} {self.aidant.last_name}" if self.aidant else None,
            'senior_name': f"{self.senior.first_name} {self.senior.last_name}" if self.senior else None
        }
    
    @staticmethod
    def get_user_appointments(user_id, status=None, limit=10):
        """Récupérer les rendez-vous d'un utilisateur"""
        query = Appointment.query.filter(
            (Appointment.aidant_id == user_id) | (Appointment.senior_id == user_id)
        )
        
        if status:
            query = query.filter_by(status=status)
        
        return query.order_by(Appointment.start_datetime.asc()).limit(limit).all()
    
    @staticmethod
    def get_upcoming_appointments(user_id, limit=5):
        """Récupérer les prochains rendez-vous d'un utilisateur"""
        now = datetime.utcnow()
        return Appointment.query.filter(
            (Appointment.aidant_id == user_id) | (Appointment.senior_id == user_id),
            Appointment.start_datetime > now,
            Appointment.status.in_(['planned', 'confirmed'])
        ).order_by(Appointment.start_datetime.asc()).limit(limit).all()


class UserAlert(db.Model):
    """Modèle pour les alertes personnalisées"""
    __tablename__ = 'user_alerts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    alert_type = db.Column(db.String(50), nullable=False)  # 'new_requests', 'new_aidants', 'matching_offers'
    criteria = db.Column(db.JSON)  # Critères de filtrage (zone géographique, compétences, etc.)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relation avec l'utilisateur
    user = db.relationship('User', backref=db.backref('alerts', lazy=True))
    
    def __repr__(self):
        return f'<UserAlert {self.id}: {self.alert_type}>'
    
    def to_dict(self):
        """Convertir l'alerte en dictionnaire"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'alert_type': self.alert_type,
            'criteria': self.criteria,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }
    
    @staticmethod
    def get_user_alerts(user_id, active_only=True):
        """Récupérer les alertes d'un utilisateur"""
        query = UserAlert.query.filter_by(user_id=user_id)
        
        if active_only:
            query = query.filter_by(is_active=True)
        
        return query.all()
