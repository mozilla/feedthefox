"""
Django settings for feedthefox project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

import dj_database_url
from decouple import Csv, config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    # Project specific apps
    'feedthefox.base',
    'feedthefox.users',
    'feedthefox.dashboard',
    'feedthefox.devices',

    # Third party apps
    'django_jinja',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.persona'
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
)

ROOT_URLCONF = 'feedthefox.urls'

WSGI_APPLICATION = 'feedthefox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=True, cast=bool)

USE_TZ = config('USE_TZ', default=True, cast=bool)

STATIC_HOST = config('STATIC_HOST', default='')
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
STATIC_URL = config('STATIC_URL', STATIC_HOST + '/static/')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = config('MEDIA_URL', '/media/')
USER_PHOTOS_DIR = config('USER_PHOTOS_DIR', MEDIA_ROOT + '/uploads/profiles')
PERSONA_AUDIENCE = config('PERSONA_AUDIENCE', default='')

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=not DEBUG, cast=bool)

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'match_extension': '.html',
            'app_dirname': 'templates/jinja2',
            'newstyle_gettext': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'feedthefox.base.context_processors.settings',
                'feedthefox.base.context_processors.i18n',
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        }
    },
]

# Custom User model
AUTH_USER_MODEL = 'users.User'

# Mozillians.org API settings
MOZILLIANS_API_URL = config('MOZILLIANS_API_URL', default=None)
MOZILLIANS_API_KEY = config('MOZILLIANS_API_KEY', default=None)

# Required by allauth
SITE_ID = 1

# Django-allauth configuration
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_ADAPTER = 'feedthefox.users.adapters.FeedTheFoxAdapter'
ACCOUNT_UNIQUE_EMAIL = True

SOCIALACCOUNT_ADAPTER = 'feedthefox.users.adapters.FeedTheFoxSocialAdapter'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_PROVIDERS = {
    'persona': {
        'AUDIENCE': PERSONA_AUDIENCE
    }
}

PERSONA_VERIFIER_URL = 'https://verifier.login.persona.org/verify'
PERSONA_INCLUDE_URL = 'https://login.persona.org/include.js'
LOGIN_REDIRECT_URL = '/profile/'

# Django-CSP
CSP_DEFAULT_SRC = (
    "'self'",
    'https://*.mozilla.org',
)

CSP_DEFAULT_SRC += tuple(config('CSP_DEFAULT_SRC', default='', cast=Csv()))

CSP_FONT_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'http://*.mozilla.org',
    'https://*.mozilla.org',
)

CSP_FONT_SRC += tuple(config('CSP_FONT_SRC', default='', cast=Csv()))

CSP_IMG_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'http://*.mozilla.org',
    'https://*.mozilla.org',
)

CSP_IMG_SRC += tuple(config('CSP_IMG_SRC', default='', cast=Csv()))

CSP_FRAME_SRC = (
    "'self'",
    'https://login.persona.org',
)

CSP_FRAME_SRC += tuple(config('CSP_FRAME_SRC', default='', cast=Csv()))

CSP_SCRIPT_SRC = (
    "'self'",
    # TODO: fix/replace this
    "'unsafe-inline'",
    'http://*.mozilla.org',
    'https://*.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://login.persona.org',
)

CSP_SCRIPT_SRC += tuple(config('CSP_SCRIPT_SRC', default='', cast=Csv()))

CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    'http://*.mozilla.org',
    'https://*.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
)

CSP_STYLE_SRC += tuple(config('CSP_STYLE_SRC', default='', cast=Csv()))

# Opbeat support
INSTALLED_APPS.append('opbeat.contrib.django')

OPBEAT = {
    'ORGANIZATION_ID': config('OPBEAT_ORGANIZATION_ID', default=''),
    'APP_ID': config('OPBEAT_APP_ID', default=''),
    'SECRET_TOKEN': config('OPBEAT_SECRET_TOKEN', default=''),
}

MIDDLEWARE_CLASSES += (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
)
