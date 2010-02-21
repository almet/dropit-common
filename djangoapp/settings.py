DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dropit.sql'

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True

MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '0#=s4i-c@^tm#*sk15%9hxhf$rwm6+$n3i$*)tbzv3*$6&$wzn'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'djangoapp.urls'

import os.path
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

STATIC_DOC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'staticfiles')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'couchdbkit.ext.django',
    'notes',
    'gunicorn',
)

COUCHDB_DATABASES = (
    ('notes', 'http://127.0.0.1:5984/dropit'),
)

NOTES_FORMATS = (
    ('markdown','Markdown'), 
    ('fulltext','Full Text'), 
    ('rst', 'ReSTructured Text')
)
