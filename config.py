import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'chicken_yasaka221')
    MONGODB_URI = os.environ.get('MONGODB_URI')
    DB_NAME = os.environ.get('DB_NAME')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Configuration for development."""
    DEBUG = True
    MONGODB_URI = os.environ.get('DEV_MONGODB_URI', Config.MONGODB_URI)
