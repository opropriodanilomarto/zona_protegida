"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from pathlib import Path

from decouple import Csv, config
from dj_database_url import parse as dburl

# CORE SETTINGS
# ---------------------------------------------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())
CSRF_COOKIE_HTTPONLY = True

# CACHE
# ---------------------------------------------------------------------------------------------------------------------
CACHE = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# DEBUG
# ---------------------------------------------------------------------------------------------------------------------
DEBUG = config("DEBUG", cast=bool)

# DATABASES
# ---------------------------------------------------------------------------------------------------------------------
DATABASES = {"default": config("DATABASE_URL", cast=dburl)}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL
# ---------------------------------------------------------------------------------------------------------------------
# Configurar a variável EMAIL_BACKEND para "django.core.mail.backends.smtp.EmailBackend" em produção ou se não for usar
# o console.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
EMAIL_USE_SSL = config("EMAIL_USE_SSL")

# FILE UPLOADS
# ---------------------------------------------------------------------------------------------------------------------
MEDIA_URL = "/media/"

# Globalization
# ---------------------------------------------------------------------------------------------------------------------
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Localization
# ---------------------------------------------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"

# HTTP
# ---------------------------------------------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware" if not DEBUG else "",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

WSGI_APPLICATION = "config.wsgi.application"
INTERNAL_IPS = ["127.0.0.1"]

# Logging
# ---------------------------------------------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": not DEBUG,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

if not DEBUG:
    LOGGING["loggers"] = {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    }

# MODELS
# ---------------------------------------------------------------------------------------------------------------------
INSTALLED_APPS = [
    "zp.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "crispy_bootstrap5",
    "zp",
]

if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

# SECURITY
# ---------------------------------------------------------------------------------------------------------------------
SECRET_KEY = config("SECRET_KEY")
X_FRAME_OPTIONS = "DENY"


# TEMPLATES
# ---------------------------------------------------------------------------------------------------------------------
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
            ],
        },
    },
]

# URLS
# ---------------------------------------------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# AUTH
# ---------------------------------------------------------------------------------------------------------------------
AUTH_USER_MODEL = "auth.User"
LOGIN_REDIRECT_URL = "zp:index"
LOGIN_URL = "zp:login"
LOGOUT_REDIRECT_URL = "zp:login"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# SESSIONS
# ---------------------------------------------------------------------------------------------------------------------
SESSION_COOKIE_HTTPONLY = True

# SITES
# ---------------------------------------------------------------------------------------------------------------------
SITE_ID = 1

# STATIC FILES
# ---------------------------------------------------------------------------------------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "node_modules",
]

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
