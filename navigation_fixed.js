/**
 * Système de navigation amélioré avec gestion complète des états utilisateur
 */

class NavigationSystem {
    constructor() {
        this.isAuthenticated = false;
        this.userType = 'senior';
        this.userName = 'Utilisateur';
        this.userEmail = '';
        this.init();
    }

    async init() {
        await this.checkAuthentication();
        this.createNavigation();
        this.setupMobileMenu();
        this.setupEventListeners();
        
        // Émettre un événement pour notifier les autres composants
        this.emitAuthStateChanged();
    }

    async checkAuthentication() {
        try {
            const response = await fetch('/api/auth/check-auth');
            if (response.ok) {
                const data = await response.json();
                this.isAuthenticated = data.authenticated || false;
                
                if (this.isAuthenticated && data.user) {
                    this.userType = data.user.user_type || 'senior';
                    this.userName = data.user.first_name || 'Utilisateur';
                    this.userEmail = data.user.email || '';
                    
                    // Sauvegarder dans localStorage
                    this.saveAuthData();
                } else {
                    // Nettoyer localStorage si pas authentifié
                    this.clearAuthData();
                }
            } else {
                // En cas d'erreur API, utiliser les données locales si disponibles
                this.loadFromLocalStorage();
            }
        } catch (error) {
            console.log('Erreur de vérification d\'authentification:', error);
            // Utiliser les données locales si disponibles
            this.loadFromLocalStorage();
        }
    }

    saveAuthData() {
        localStorage.setItem('isAuthenticated', 'true');
        localStorage.setItem('userType', this.userType);
        localStorage.setItem('userName', this.userName);
        localStorage.setItem('userEmail', this.userEmail);
    }

    loadFromLocalStorage() {
        this.isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
        this.userType = localStorage.getItem('userType') || 'senior';
        this.userName = localStorage.getItem('userName') || 'Utilisateur';
        this.userEmail = localStorage.getItem('userEmail') || '';
    }

    clearAuthData() {
        this.isAuthenticated = false;
        this.userType = 'senior';
        this.userName = 'Utilisateur';
        this.userEmail = '';
        
        localStorage.removeItem('isAuthenticated');
        localStorage.removeItem('userType');
        localStorage.removeItem('userName');
        localStorage.removeItem('userEmail');
    }

    createNavigation() {
        const existingNav = document.querySelector('.main-navigation');
        if (existingNav) {
            existingNav.remove();
        }

        const nav = document.createElement('nav');
        nav.className = 'main-navigation';
        nav.innerHTML = this.getNavigationHTML();

        // Insérer la navigation au début du body
        document.body.insertBefore(nav, document.body.firstChild);
        
        // Ajouter les styles
        this.addNavigationStyles();
    }

    getNavigationHTML() {
        const logoLink = this.isAuthenticated ? 'dashboard.html' : 'index.html';
        
        if (this.isAuthenticated) {
            return `
                <div class="nav-content-official">
                    <div class="nav-logo-official">
                        <a href="${logoLink}" class="logo-link-official">
                            <img src="logo_assemblage_nouveau.png" alt="Assembl'âge Employeur-Employés" class="logo-img-official">
                        </a>
                    </div>
                    
                    <div class="nav-links-official">
                        <a href="dashboard.html" class="nav-btn-official nav-dashboard">Tableau de bord</a>
                        <a href="my-service-offers.html" class="nav-btn-official nav-offers">Mes offres</a>
                        <a href="search-real-map.html" class="nav-btn-official nav-search">Recherche</a>
                        <a href="messages-fixed.html" class="nav-btn-official nav-messages">
                            Messages
                            <span class="message-count">0</span>
                        </a>
                        <a href="profile-corrected.html" class="nav-btn-official nav-profile">Mon profil</a>
                    </div>

                    <div class="nav-user-info">
                        <span class="user-name-official">${this.userName}</span>
                        <span class="user-badge-official">${this.userRole}</span>
                    </div>
                    
                    <button class="nav-btn-logout" onclick="logout()">Déconnexion</button>
                    
                    <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>
            `;bile-menu-toggle">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>

                <div class="mobile-menu">
                    <a href="dashboard.html" class="nav-link">
                        <i class="fas fa-home"></i> Tableau de bord
                    </a>
                    <a href="my-service-offers.html" class="nav-link">
                        <i class="fas fa-edit"></i> Mes offres
                    </a>
                    <a href="search-real-map.html" class="nav-link">
                        <i class="fas fa-search"></i> Recherche
                    </a>
                    <a href="messages-fixed.html" class="nav-link">
                        <i class="fas fa-comments"></i> Messages
                    </a>
                    <a href="profile-corrected.html" class="nav-link">
                        <i class="fas fa-user"></i> Mon profil
                    </a>
                    <button onclick="logout()" class="nav-link logout-mobile">
                        <i class="fas fa-sign-out-alt"></i> Déconnexion
                    </button>
                </div>
            `;
        } else {
            return `
                <div class="nav-content-official">
                    <div class="nav-logo-official">
                        <a href="${logoLink}" class="logo-link-official">
                            <img src="logo_assemblage_nouveau.png" alt="Assembl'âge Employeur-Employés" class="logo-img-official">
                        </a>
                    </div>
                    
                    <div class="nav-links-official">
                        <a href="index.html" class="nav-btn-official nav-accueil">Accueil</a>
                        <a href="index.html#services" class="nav-btn-official nav-publications">Services</a>
                        <a href="index.html#how-it-works" class="nav-btn-official nav-missions">Comment ça marche</a>
                        <a href="login.html" class="nav-btn-official nav-btn-contact">Contact</a>
                    </div>

                    <button class="mobile-menu-toggle" onclick="toggleMobileMenu()">
                        <span></span>
                        <span></span>
                        <span></span>
                    </button>
                </div>

                <div class="mobile-menu">
                    <a href="index.html" class="nav-link">Accueil</a>
                    <a href="index.html#services" class="nav-link">Services</a>
                    <a href="index.html#how-it-works" class="nav-link">Comment ça marche</a>
                    <a href="login.html" class="nav-link">Contact</a>
                </div>
            `;
        }
    }

    emitAuthStateChanged() {
        const event = new CustomEvent('authStateChanged', {
            detail: {
                isAuthenticated: this.isAuthenticated,
                userType: this.userType,
                userName: this.userName,
                userEmail: this.userEmail
            }
        });
        window.dispatchEvent(event);
    }

    setupEventListeners() {
        // Écouter les changements de localStorage
        window.addEventListener('storage', (e) => {
            if (e.key === 'isAuthenticated') {
                this.checkAuthentication().then(() => {
                    this.createNavigation();
                    this.emitAuthStateChanged();
                });
            }
        });

        // Écouter les événements de déconnexion
        window.addEventListener('logout', () => {
            this.clearAuthData();
            this.createNavigation();
            this.emitAuthStateChanged();
        });
    }

    setupMobileMenu() {
        const toggle = document.querySelector('.mobile-menu-toggle');
        const mobileMenu = document.querySelector('.mobile-menu');
        
        if (toggle && mobileMenu) {
            toggle.addEventListener('click', () => {
                mobileMenu.classList.toggle('active');
                toggle.classList.toggle('active');
            });

            // Fermer le menu mobile lors du clic sur un lien
            mobileMenu.querySelectorAll('.nav-link').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.remove('active');
                    toggle.classList.remove('active');
                });
            });
        }
    }

    addNavigationStyles() {
        // Supprimer les anciens styles s'ils existent
        const existingStyle = document.getElementById('navigation-styles');
        if (existingStyle) {
            existingStyle.remove();
        }

        const style = document.createElement('style');
        style.id = 'navigation-styles';
        style.textContent = `
            .main-navigation {
                background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                position: sticky;
                top: 0;
                z-index: 1000;
                font-family: 'Montserrat', sans-serif;
            }

            .nav-content {
                max-width: 1200px;
                margin: 0 auto;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 2rem;
                height: 70px;
            }

            .nav-brand .brand-link {
                display: flex;
                align-items: center;
                text-decoration: none;
                color: white;
                font-weight: 700;
                font-size: 1.5rem;
            }

            .brand-icon {
                background: white;
                color: #4CAF50;
                width: 40px;
                height: 40px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 0.75rem;
                font-weight: bold;
            }

            .nav-desktop {
                display: flex;
                align-items: center;
                gap: 2rem;
            }

            .nav-links {
                display: flex;
                align-items: center;
                gap: 1.5rem;
            }

            .nav-link {
                color: white;
                text-decoration: none;
                padding: 0.5rem 1rem;
                border-radius: 6px;
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                font-weight: 500;
                position: relative;
            }

            .nav-link:hover {
                background: rgba(255,255,255,0.1);
                transform: translateY(-1px);
            }

            .message-count {
                background: #ff4444;
                color: white;
                border-radius: 50%;
                padding: 0.2rem 0.5rem;
                font-size: 0.8rem;
                min-width: 20px;
                text-align: center;
            }

            .nav-actions {
                display: flex;
                align-items: center;
                gap: 1rem;
            }

            .user-info {
                display: flex;
                flex-direction: column;
                align-items: flex-end;
                color: white;
            }

            .user-name {
                font-weight: 600;
                font-size: 0.9rem;
            }

            .user-type {
                font-size: 0.8rem;
                opacity: 0.8;
                text-transform: capitalize;
            }

            .logout-btn, .login-btn {
                background: rgba(255,255,255,0.1);
                border: 2px solid rgba(255,255,255,0.3);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 6px;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                display: flex;
                align-items: center;
                gap: 0.5rem;
                font-weight: 500;
            }

            .logout-btn:hover, .login-btn:hover {
                background: rgba(255,255,255,0.2);
                border-color: rgba(255,255,255,0.5);
                transform: translateY(-1px);
            }

            .mobile-menu-toggle {
                display: none;
                flex-direction: column;
                background: none;
                border: none;
                cursor: pointer;
                padding: 0.5rem;
            }

            .mobile-menu-toggle span {
                width: 25px;
                height: 3px;
                background: white;
                margin: 3px 0;
                transition: 0.3s;
                border-radius: 2px;
            }

            .mobile-menu-toggle.active span:nth-child(1) {
                transform: rotate(-45deg) translate(-5px, 6px);
            }

            .mobile-menu-toggle.active span:nth-child(2) {
                opacity: 0;
            }

            .mobile-menu-toggle.active span:nth-child(3) {
                transform: rotate(45deg) translate(-5px, -6px);
            }

            .mobile-menu {
                display: none;
                background: #4CAF50;
                border-top: 1px solid rgba(255,255,255,0.1);
            }

            .mobile-menu.active {
                display: block;
            }

            .mobile-menu .nav-link, .logout-mobile {
                display: block;
                padding: 1rem 2rem;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                color: white;
                text-decoration: none;
                background: none;
                border: none;
                width: 100%;
                text-align: left;
                cursor: pointer;
                font-family: inherit;
                font-size: inherit;
            }

            .mobile-menu .nav-link:hover, .logout-mobile:hover {
                background: rgba(255,255,255,0.1);
            }

            @media (max-width: 768px) {
                .nav-desktop {
                    display: none;
                }

                .mobile-menu-toggle {
                    display: flex;
                }

                .nav-content {
                    padding: 0 1rem;
                }

                .brand-text {
                    display: none;
                }
            }
        `;
        document.head.appendChild(style);
    }
}

// Fonction de déconnexion globale améliorée
async function logout() {
    try {
        // Afficher une notification de déconnexion
        if (window.RedirectNotification) {
            window.RedirectNotification.show('Déconnexion en cours...', 'info');
        }

        const response = await fetch('/api/auth/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Nettoyer le stockage local dans tous les cas
        localStorage.clear();
        sessionStorage.clear();
        
        // Émettre un événement de déconnexion
        const logoutEvent = new CustomEvent('logout');
        window.dispatchEvent(logoutEvent);
        
        // Rediriger vers l'accueil avec un délai
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 500);
        
    } catch (error) {
        console.error('Erreur lors de la déconnexion:', error);
        // Forcer la déconnexion locale même en cas d'erreur
        localStorage.clear();
        sessionStorage.clear();
        
        const logoutEvent = new CustomEvent('logout');
        window.dispatchEvent(logoutEvent);
        
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 500);
    }
}

// Initialiser la navigation quand le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
    new NavigationSystem();
});

// Exporter pour utilisation globale
window.NavigationSystem = NavigationSystem;
window.logout = logout;


// Fonction pour le menu burger mobile
function toggleMobileMenu() {
    const navLinks = document.querySelector('.nav-links-official');
    const menuToggle = document.querySelector('.mobile-menu-toggle');
    
    if (navLinks && menuToggle) {
        navLinks.classList.toggle('mobile-open');
        menuToggle.classList.toggle('open');
    }
}

// Fermer le menu mobile quand on clique sur un lien
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-btn-official');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            const navLinksContainer = document.querySelector('.nav-links-official');
            const menuToggle = document.querySelector('.mobile-menu-toggle');
            
            if (navLinksContainer && menuToggle) {
                navLinksContainer.classList.remove('mobile-open');
                menuToggle.classList.remove('open');
            }
        });
    });
    
    // Fermer le menu mobile quand on clique en dehors
    document.addEventListener('click', function(event) {
        const navLinksContainer = document.querySelector('.nav-links-official');
        const menuToggle = document.querySelector('.mobile-menu-toggle');
        const navigation = document.querySelector('.main-navigation');
        
        if (navLinksContainer && menuToggle && navigation) {
            if (!navigation.contains(event.target)) {
                navLinksContainer.classList.remove('mobile-open');
                menuToggle.classList.remove('open');
            }
        }
    });
});
