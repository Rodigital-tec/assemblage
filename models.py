# Re-export all models from the models package
# This file allows importing models directly from the models module

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Import all models
try:
    from user import User, Availability
    from help_request import HelpRequest, HelpRequestTimeSlot, HelpOffer
    from message import Message, AdminMessage
    from config import SMTPConfig, ActivityLog
    from service_type import ServiceType, HelpRequestService
    from service_offer import ServiceOffer, service_offer_services
    from admin import Admin, AuditLog, SystemConfig, AdminRole
    from support_ticket import SupportTicket, TicketMessage, UserReport, TicketStatus, TicketPriority, TicketCategory
    from analytics import DailyStats, UserActivity, SystemMetrics, EmailLog
    from notification import Notification
except ImportError:
    # If models are in a models package, try importing from there
    try:
        from models.user import User, Availability
        from models.help_request import HelpRequest, HelpRequestTimeSlot, HelpOffer
        from models.message import Message, AdminMessage
        from models.config import SMTPConfig, ActivityLog
        from models.service_type import ServiceType, HelpRequestService
        from models.service_offer import ServiceOffer, service_offer_services
        from models.admin import Admin, AuditLog, SystemConfig, AdminRole
        from models.support_ticket import SupportTicket, TicketMessage, UserReport, TicketStatus, TicketPriority, TicketCategory
        from models.analytics import DailyStats, UserActivity, SystemMetrics, EmailLog
        from models.notification import Notification
    except ImportError:
        # If still not found, create placeholder models
        print("Warning: Could not import models. Using placeholder models.")
        
        class User(db.Model):
            __tablename__ = 'users'
            id = db.Column(db.Integer, primary_key=True)
            email = db.Column(db.String(255), unique=True, nullable=False)
            password_hash = db.Column(db.String(255), nullable=False)
            first_name = db.Column(db.String(255))
            last_name = db.Column(db.String(255))
            user_type = db.Column(db.String(50))
            is_active = db.Column(db.Boolean, default=True)
            email_verified = db.Column(db.Boolean, default=False)
        
        class SMTPConfig(db.Model):
            __tablename__ = 'smtp_config'
            id = db.Column(db.Integer, primary_key=True)
            smtp_server = db.Column(db.String(255))
            smtp_port = db.Column(db.Integer)
            smtp_username = db.Column(db.String(255))
            smtp_password = db.Column(db.String(255))
            use_tls = db.Column(db.Boolean, default=True)
        
        class HelpRequest(db.Model):
            __tablename__ = 'help_requests'
            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String(255))
            description = db.Column(db.Text)
            user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

__all__ = [
    'db',
    'User',
    'SMTPConfig',
    'HelpRequest',
]

