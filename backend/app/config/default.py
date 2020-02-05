import os

class Config():
    DEBUG = True
    Host = '0.0.0.0'
    Port = 8089
    MONGODB_SETTINGS = {
        'db': 'sheroa3',
        'host': 'mongodb://localhost:27017/sheroa3',
    }
    JWT_SECRET = "sheroa3@lymnb.*&"