class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_ECHO = False
    
    # Enhanced security for production
    PREFERRED_URL_SCHEME = 'https'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Strong secrets (safe defaults so app won't crash)
    SECRET_KEY = os.getenv('SECRET_KEY', Config.SECRET_KEY)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', Config.JWT_SECRET_KEY)

    # SQLAlchemy connection pool settings
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "pool_timeout": 30,
        "pool_recycle": 1800,
        "max_overflow": 20,
    }

    # Logging configuration
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/app.log'

    # Email configuration (SMTP)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # CORS configuration
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')
    
    # Rate limiting (if using Flask-Limiter)
    RATELIMIT_DEFAULT = "200 per day;50 per hour"


def setup_logging(app):
    """Configure logging for the Flask application"""
    from logging.handlers import RotatingFileHandler
    import logging
    
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    handler = RotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        maxBytes=100000,
        backupCount=3
    )
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)  # ✅ ensure logs show up

