import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True

db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']
API_TITLE = "backend-labs"
API_VERSION = "1.0.0"
OPENAPI_VERSION = "3.0.3"
SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False