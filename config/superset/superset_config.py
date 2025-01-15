import os

# Branding
APP_NAME = "PLED Analytics"
APP_ICON = "/static/assets/images/pled_logo.png"

# Authentication
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

# Database configurations
SQLALCHEMY_DATABASE_URI = os.environ.get('SUPERSET_DB_URI')

# BigQuery connection string will be configured via UI
