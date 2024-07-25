import os
from dotenv import load_dotenv

from helpers.utils import str_to_bool

SRS_VERSION_NAME = "v0.9.0"
SRS_VERSION_NUMBER = 900

load_dotenv()


DATABASE_SETTINGS = {
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "database": os.getenv("DATABASE_NAME"),
    "port": int(os.getenv("DATABASE_PORT")),
}

TORTOISE_CONFIG = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': DATABASE_SETTINGS.get('host'),
                'port': DATABASE_SETTINGS.get('port'),
                'user': DATABASE_SETTINGS.get('user'),
                'password': DATABASE_SETTINGS.get('password'),
                'database': DATABASE_SETTINGS.get('database'),
            }
        },
    },
    'apps': {
        'models': {
            'models': ["database.models", "aerich.models"],
            'default_connection': 'default',
        }
    }
}

DEBUG = str_to_bool(os.getenv('DEBUG', 'False'))

# ENDPOINT SPECIFIC SETTINGS:
# Defines behaviour for narrative generation, helpful for limiting costs
# during the testing phase:
GENERATE_SHORTER_NARRATIVES = str_to_bool(os.getenv('GENERATE_SHORTER_NARRATIVES', 'True'))
