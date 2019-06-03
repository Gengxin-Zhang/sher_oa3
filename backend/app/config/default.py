import os

class Config():
    Debug = True
    HOST = '127.0.0.1'
    PORT = 9098
    MONGODB_SETTINGS = {
        'db': 'sheroa3',
        'host': 'mongodb://localhost:27017/sheroa3',
    }