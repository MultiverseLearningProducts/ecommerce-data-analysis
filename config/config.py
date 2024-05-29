import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('postgres', 'username')
password = config.get('postgres' 'password')
host = config.get('postgres', 'host')
port = config.get('postgres', 'port')

DATABASE_URI = f'postgresql://{username}:{password}@{host}:{port}/mydatabase'
AWS_REGION = config.get('aws', 'region')
S3_BUCKET_NAME = config.get('aws', 'bucket_name')
S3_OUTPUT_FILE = config.get('aws', 'output')


