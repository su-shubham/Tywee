import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_HOSTNAME = os.getenv('DATABASE_HOSTNAME', 'localhost')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'shubham')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'root')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'ecommerce')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'test_ecommerce')
REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
REDIS_DB = os.getenv('REDIS_DB', '0')
