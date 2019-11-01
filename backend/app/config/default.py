import os

class Config():
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8089
    MONGODB_SETTINGS = {
        'db': 'sheroa3',
        'host': 'mongodb://localhost:27017/sheroa3',
    }
    JWT_SECRET = "sheroa3@lymnb.*&"