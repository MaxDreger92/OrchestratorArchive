"""
Django settings for mat2devplatform project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from decouple import Csv, config
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment.")
    # 'django-insecure-#3zy6e+h5%+*0=5j6mp5%)9g#0ss1^dgocst79g9dg*c6c&@-+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000000

GITHUB_WEBHOOK_SECRET = config(os.getenv('GITHUB_WEBHOOK_SECRET'), default='')


ALLOWED_HOSTS = ["134.94.199.247", "127.0.0.1", "localhost", "matgraph.xyz"]

#Openai API Key

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '../debug.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Application definition

INSTALLED_APPS = [
    'mat2devplatform',
    'default',
    'matching',
    'usermanagement',
    'importing',
    'matgraph',
    'graphutils',
    'colorfield',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'dbcommunication',
    'django_neomodel',
    'django_cleanup.apps.CleanupConfig',
    'django_admin_multiple_choice_list_filter',
    'nested_admin',
    'django_summernote',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_filters',
    'django_extensions',
    'related_admin',
    'admin_interface',
    'dal',
    'dal_select2',
    'rest_framework'
]

AUTH_USER_MODEL = 'usermanagement.CustomUser'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = 'home'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# you are free to add this configurations
NEOMODEL_NEO4J_BOLT_URL = os.environ.get(
    'NEO4J_BOLT_URL', os.getenv('NEOMODEL_NEO4J_BOLT_URL'))
NEOMODEL_SIGNALS = True
NEOMODEL_FORCE_TIMEZONE = False
NEOMODEL_ENCRYPTED_CONNECTION = True
NEOMODEL_MAX_POOL_SIZE = 50

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'mat2devplatform.urls'
# OpenAI API Key
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR) + '/templates/', str(BASE_DIR) + '/frontend/build/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mat2devplatform.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'herrklo1',
        'HOST': 'localhost',
    },
    'neo4j': {
        'ENGINE': '',
        'NAME': 'neo4j',
        'NEOMODEL_NEO4J_BOLT_URL': NEOMODEL_NEO4J_BOLT_URL,
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mat2devplatform/static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build'),
    os.path.join(BASE_DIR, 'matching/static'),
    ]
print(STATICFILES_DIRS)
# Media Files
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
