"""
Django settings for mysite project.
Generated by 'django-admin startproject' using Django 2.1.3.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ


# load .env file, which contains sensitive information that we don't want uploaded to github or AWS
environ.Env.read_env()

# required for tracking DEBUG value in templates
# Reference: https://stackoverflow.com/questions/1271631/how-to-check-the-template-debug-flag-in-a-django-template/1271914
INTERNAL_IPS = (
    '127.0.0.1',
)

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# False if not in os.environ
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
DEBUG = False


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = [ '127.0.0.1', 'localhost', '.amazonaws.com', '.lawrencemcdaniel.com', ]


# Application definition

INSTALLED_APPS = [
    'pipeline',
    'djangobower',
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.gzip.GZipMiddleware',
#    'pipeline.middleware.MinifyHTMLMiddleware',
]

ROOT_URLCONF = 'urls'

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

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('RDS_DB_NAME'),
        'USER': env('RDS_USERNAME'),
        'PASSWORD': env('RDS_PASSWORD'),
        'HOST': env('RDS_HOSTNAME'),
        'PORT': env('RDS_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


#======================= Static runt-time config ================================
# Static files (CSS, JavaScript, Images)
# Reference: https://docs.djangoproject.com/en/2.1/howto/static-files/
#================================================================================
if DEBUG:
    STATIC_URL = '/static/'
else:
    STATIC_URL = 'https://s3-us-west-2.amazonaws.com/zappa-bg95bqbw1/static/'


#======================= collectstatic config ================================
# Static files (CSS, JavaScript, Images)
# Reference: https://docs.djangoproject.com/en/2.1/howto/static-files/
#======================= collectstatic config ================================

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# tell django the full path to the location of all static assets
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'mysite', 'polls', 'staticfiles'),
]

#tell django where to look when running collectstatic - via custom classes
STATICFILES_FINDERS = (
    'djangobower.finders.BowerFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'pipeline.finders.PipelineFinder',
)
#Reference: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.ManifestStaticFilesStorage
# XXX STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineCachedStorage'

#STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
#STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

#======================= Pipeline Setup ================================
# Reference: https://django-pipeline.readthedocs.io/en/latest/
#    'COMPILERS': {
#        'pipeline.compilers.sass.SASSCompiler',
#    },
#
#    'PIPELINE_ENABLED': True,
#======================= Pipeline Setup ================================
PIPELINE = {
    'CSS_COMPRESSOR': 'pipeline.compressors.yuglify.YuglifyCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.JSMinCompressor',
    'STYLESHEETS': {
        'pollsX': {
            'source_filenames': (
              'bootstrap/dist/css/bootstrap.css',
              'css/mystyles.css'
            ),
            'output_filename': 'styles.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'pollsX': {
            'source_filenames': (
              'jquery/dist/jquery.js',
              'popper.js/dist/popper.js',
              'bootstrap/dist/js/bootstrap.js',
              'js/myscripts.js'
            ),
            'output_filename': 'bundle.js',
        }
    }
}


#======================= Bower Setup ================================
# Reference: https://django-bower.readthedocs.io/en/latest/installation.html
#======================= Bower Setup ================================
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
#BOWER_PATH = '/usr/bin/bower'          # we might not need thisself.
BOWER_INSTALLED_APPS = (
    'jquery',
    'popper.js',
    'bootstrap',
    'underscore',
    'd3',
)
