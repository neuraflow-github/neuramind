import os

import firebase_admin
from firebase_admin import firestore

from common.config import config


class Firebase:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Firebase, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        if not firebase_admin._apps:
            # Check if running in Cloud Run
            if os.environ.get("K_SERVICE"):
                # Use default credentials
                self.app = firebase_admin.initialize_app()
            else:
                credentials = credentials.Certificate(config.firebase_credentials_path)
                self.app = firebase_admin.initialize_app(credentials)
        else:
            self.app = firebase_admin.get_app()
        self.db = firestore.client(self.app)


firebase = Firebase()
