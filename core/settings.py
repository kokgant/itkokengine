# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - Kokgant
"""

import logging
from os import set_inheritable
from .log_config import log_config


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #"django_celery_results",
    #"django_celery_beat",
    "admin_volt.apps.AdminVoltConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "django_extensions",
    "log_viewer",
    "corsheaders",
    # local
    "apps.itkokengine",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True



# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:8001',
#     '46.27.203.39',
# ]

# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]

ROOT_URLCONF = "core.urls"
#LOGIN_REDIRECT_URL = "login"  # Route defined in app/urls.py
#LOGOUT_REDIRECT_URL = "logout"  # Route defined in app/urls.py

WSGI_APPLICATION = "core.wsgi.application"

IMPORT_EXPORT_USE_TRANSACTIONS = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "es"
TIME_ZONE = "Europe/Madrid"
USE_I18N = True
USE_L10N = True
USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         #"rest_framework.authentication.SessionAuthentication",
#         #"rest_framework.authentication.TokenAuthentication",
#     ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
#         # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
#         # "rest_framework.permissions.DjangoModelPermissions",
    ],
#     "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
#     "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

# Config django log viewer
# url global path
# settings installed apps
#LOG_VIEWER_FILES = ['logfile1', 'logfile2', ...]
LOG_VIEWER_FILES_PATTERN = '*.log*'
LOG_VIEWER_FILES_DIR = 'logs/'
LOG_VIEWER_PAGE_LENGTH = 25       # total log lines per-page
LOG_VIEWER_MAX_READ_LINES = 1000  # total log lines will be read
LOG_VIEWER_PATTERNS = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']

# Optionally you can set the next variables in order to customize the admin:
#LOG_VIEWER_FILE_LIST_TITLE = "Custom title"
#LOG_VIEWER_FILE_LIST_STYLES = "/static/css/my-custom.css"

try:
    from .local_settings import *
except Exception as e:
    pass

try:
    logging.config.dictConfig(log_config)
except ImportError as imp_err:
    pass
