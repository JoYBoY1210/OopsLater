"""
Django settings for OopsLater project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9s1^g-ckbm(1a%b^baq+y3v%p9hv(ps6y5z4l6dj13i-dq9*ve'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://0.0.0.0" 
]    

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos',
    'rest_framework',
    'rest_framework.authtoken',
    'Authentication',
    'corsheaders',
    'django_extensions',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Leave empty if you don't have custom template directories
        'APP_DIRS': True,  # Set to True if your templates are inside apps
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


# # CSRF Settings
# CSRF_COOKIE_SAMESITE = 'Lax'  # or 'Lax' if you are not using HTTPS
# CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",  # Frontend origin
    "http://localhost:8000",  # Backend origin
    "http://127.0.0.1:8000", # Localhost backup
]

# CSRF_COOKIE_NAME = "csrftoken"
# CSRF_EXEMPT_VIEW = False  # Do not exempt CSRF protection for views

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Frontend origin
]

CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = [
    'Content-Type',
    'X-CSRFToken',  # Expose CSRF token to frontend
]
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]

# CORS_ALLOW_HEADERS = [
#     'content-type',
#     'x-csrftoken',  # Allow CSRF token header
#     'authorization',
# ]

# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # 30 days session duration
# SESSION_COOKIE_SAMESITE = 'Lax'  # Use 'None' only if using HTTPS
# SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'OopsLater.urls'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
