import os

class Config:
    def __init__(self):
        """Base configuration variables."""
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
        
        self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
        self.LOGGLY_TOKEN = os.getenv('LOGGLY_TOKEN')
