"""Django settings for config project."""

from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as db_url

# Core Settings
###############################################################################################

BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Cache
###############################################################################################
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}

# Database
###############################################################################################
DATABASES = {"default": config("DATABASE_URL", cast=db_url)}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Debugging
###############################################################################################
DEBUG = config("DEBUG", cast=bool)

# Email
###############################################################################################

# Error reporting
###############################################################################################

# File uploads
###############################################################################################

# Forms
###############################################################################################

# Globalization
###############################################################################################
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# HTTP
###############################################################################################
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
WSGI_APPLICATION = "config.wsgi.application"

# Logging
###############################################################################################

# Models
###############################################################################################
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Security
###############################################################################################
SECRET_KEY = config("SECRET_KEY")

# Serialization
###############################################################################################

# Templates
###############################################################################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Testing
###############################################################################################

# URLs
###############################################################################################
ROOT_URLCONF = "config.urls"

# Auth
###############################################################################################
AUTH_USER_MODEL = "auth.User"
LOGIN_REDIRECT_URL = ""
LOGIN_URL = ""
LOGOUT_REDIRECT_URL = ""
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Messages
###############################################################################################

# Sessions
###############################################################################################

# Sites
###############################################################################################

# Static Files
###############################################################################################
STATIC_URL = "static/"
