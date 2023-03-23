@@ -0,0 +1,9 @@
#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsu  
 BIN +45 Bytes (100%) 
littlelemon/__pycache__/settings.cpython-39.pyc
Comment on this file
Binary file not shown.
  24  
littlelemon/settings.py
Comment on this file
@@ -11,21 +11,25 @@
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j%3net^7$o5w$hx#5jqb+w$7n6s$h1&ffd$6up2g7t!0jhgg4o"
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')


# Application definition
@@ -47,6 +51,7 @@

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
@@ -88,14 +93,7 @@


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'admindjango',
        'PASSWORD' : 'employee@123!',
    }
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}

# Password validation
@@ -166,4 +164,6 @@

DJOSER={
    "USER_ID_FIELD":"username"
}
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
 BIN +196 Bytes (110%) 
requirements.txt