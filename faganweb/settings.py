"""
Django settings for faganweb project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from django.core.management.utils import get_random_secret_key
from pathlib import Path
from dotenv import load_dotenv
import os
import sys
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-$dz$_ttpn^5n)4j&9g-9lgabnezpe+dv9ekzz*vx-eajv!*i_1'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.getenv("DEBUG", "False") == "True"

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition

INSTALLED_APPS = [
    # My apps
    'learning_logs',
    'users',
    'appslist',
    'beat_the_odds',

    
    # Third party apps
    'bootstrap4',
    'django_apscheduler',

    # Default django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'faganweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'faganweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {

#            "ENGINE": "django.db.backends.sqlite3",
#            "NAME": os.path.join(BASE_DIR, "db.sqlite3")

            "ENGINE": "django.db.backends.postgresql",
            "USER" : "jfagan",
            "PASSWORD" : "JjfAff83!",
            "HOST" : "localhost",
            "PORT" : "5432",
            "NAME": "faganweb",
        }
    }

# The "len (sys.argv) == 1" condition below had to be added to allow Django ORM-enabled
# scripts to run on Digital Ocean

elif sys.argv[0] == 'manage.py' and sys.argv[1] == 'collectstatic'  or  len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
# elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        # "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),

        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "USER" : "db",
            "PASSWORD" : "AVNS_dNGJh8FbV5U7lzbvK_C",
            "HOST" : "app-5df5d195-9151-4927-948a-b5f52a3eb088-do-user-13406293-0.b.db.ondigitalocean.com",
            "PORT" : "25060",
            "NAME": "db",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True

SCHEDULER_DEFAULT = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# My settings
LOGIN_URL = 'users:login'
