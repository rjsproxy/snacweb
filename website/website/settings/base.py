import os
#from django.utils.crypto import get_random_string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read secret key from file,
#SECRET_FILE = os.path.join(BASE_DIR, 'website/secrets/secret-key.txt')
#try:
#    fd = os.open(SECRET_FILE,os.O_RDONLY)
#    SECRET_KEY = os.read(fd,512)
#    os.close(fd)
#except OSError:
#    try:
#        SECRET_KEY = get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
#        fd = os.open(SECRET_FILE,os.O_WRONLY|os.O_CREAT,0400)
#        os.write(fd, SECRET_KEY)
#        os.close(fd)
#    except OSError:
#         Exception('Unable to read or generate generate SECRETE_KEY file %s.' % SECRET_FILE) 

ALLOWED_HOSTS = ['.snac.unimelb.edu.au']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-filer
        #'filer',
        #'easy_thumbnails',
    # Flatpages.
    'django.contrib.sites',
    'django.contrib.flatpages',
    # Asset Management
    'djangobower',
    #'compressor', replaced with gulp
    # CKEditor
    'ckeditor',
    'snac',
    # Thumnails
    'sorl.thumbnail',
    # Bourbon.
    #'bourbon', replaced with git clone
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # flatpages.
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATI#C

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    #'compressor.finders.CompressorFinder',
)

# MEDIA

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

# django-filer / django-thumbnails

    # Overkill for our needs. Didn't really get thumnail generation working.

    #THUMBNAIL_HIGH_RESOLUTION = True
    #THUMBNAIL_PROCESSORS = (
    #    'easy_thumbnails.processors.colorspace',
    #    'easy_thumbnails.processors.autocrop',
    #    #'easy_thumbnails.processors.scale_and_crop',
    #    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    #    'easy_thumbnails.processors.filters',
    #)

# Asset Management

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, '../components')
BOWER_INSTALLED_APPS = (
    'modernizr',
    'holderjs',
    #'html5shiv',  not sure if I need this... modernizr might cover.
)

COMPRESS_ENABLED = True
COMPRESS_URL = STATIC_URL
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'snac.compressor_filters.PatchedSCSSCompiler'),
)
COMPRESS_CSS_FILTERS = (
    'snac.compressor_filters.CustomCssAbsoluteFilter',
)


# django-ckeditor


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
# CKEDITOR_RESTRICT_BY_USER = False
# http://docs.cksource.com/CKEditor_3.x/Developers_Guide/Setting_Configurations
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker'],
                    ['NumberedList', 'BulletedList', 'Indent', 'Outdent', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ['Image', 'Table', 'Link', 'Unlink', 'Anchor', 'SectionLink', 'Subscript', 'Superscript'],
                    ['Undo', 'Redo'], ['Source'], ['Maximize']],
        'filebrowserUploadUrl': '',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '/ckeditor/browse/',
        "filebrowserImageUploadUrl": "/ckeditor/upload/"
        #'extraPlugins': 'maximize',
    },
}

# django-contrib-flatpages

SITE_ID=1






# LOGGING

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': os.path.join(BASE_DIR, '../../log/django.log'),
#        },
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['file'],
#            'level': 'DEBUG',
#            'propagate': True,
#        },
#    },
#}


# Logging to stderr should end up in "/var/log/apache/error.log".

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            # 'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
