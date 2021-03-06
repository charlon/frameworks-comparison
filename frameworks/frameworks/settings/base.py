"""
Django settings for frameworks project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ni9kzpv*6cit_-mb#1-1g3diy8j!!actv!(6h!=vi8d(wufui^'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #libs
    'compressor',
    'easy_pjax',
    'rest_framework',
    'templatetag_handlebars',
    'turbolinks',
    
    #apps
    'stampos',
    #'angular',
    #'ember',
    #'backbone',
    'handlebars',
    'pjax',
    'turbo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'django_mobileesp.middleware.UserAgentDetectionMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',
)

ROOT_URLCONF = 'frameworks.urls'

WSGI_APPLICATION = 'frameworks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    #os.path.join(BASE_DIR, 'angular', 'static'),
    #os.path.join(BASE_DIR, 'ember', 'static'),
    #os.path.join(BASE_DIR, 'backbone', 'static'),
    os.path.join(BASE_DIR, 'handlebars', 'static'),
    os.path.join(BASE_DIR, 'pjax', 'static'),
    os.path.join(BASE_DIR, 'turbo', 'static'),
)

# django mobileesp

from django_mobileesp.detector import agent

DETECT_USER_AGENTS = {
    'is_tablet' : agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}


# template context processors

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    #os.path.join(BASE_DIR, 'angular', 'templates'),
    #os.path.join(BASE_DIR, 'ember', 'templates'),
    #os.path.join(BASE_DIR, 'backbone', 'templates'),
    os.path.join(BASE_DIR, 'handlebars', 'templates'),
    os.path.join(BASE_DIR, 'pjax', 'templates'),
    os.path.join(BASE_DIR, 'turbo', 'templates'),
)
