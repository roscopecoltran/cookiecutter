from os import environ
from os.path import dirname, join

from .common import *

from boto.s3.connection import SubdomainCallingFormat
import dj_database_url


DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False
LOCAL_SERVER = bool(int(environ.get('LOCAL_SERVER', '1')))

# load local .env
if LOCAL_SERVER:
    import dotenv
    PROJECT_PATH = dirname(dirname(dirname(__file__)))
    dotenv.load_dotenv(join(PROJECT_PATH, ".env"))


# Database

DATABASES = {
    'default': dj_database_url.config(default='')
}


# Apps
INSTALLED_APPS = INSTALLED_APPS + (
    # add production apps here
)


# Security

ALLOWED_HOSTS = (
    '{{ cookiecutter.domain_name }}',
)


# Storage

# use Amazon S3 for storage for uploaded media files and static files
DEFAULT_FILE_STORAGE = 'libs.s3_storages.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Amazon S3

# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
AWS_S3_CALLING_FORMAT = SubdomainCallingFormat()

AWS_ACCESS_KEY_ID = environ.get("AWS_S3_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_HOST = environ.get("AWS_S3_HOST", "s3.amazonaws.com")
AWS_AUTO_CREATE_BUCKET = False
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = True
AWS_PRELOAD_METADATA = True
AWS_REDUCED_REDUNDANCY = False

# AWS cache settings, don't change unless you know what you're doing
AWS_IS_GZIPPED = False
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY,
        AWS_EXPIREY)
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME


# Sorl

THUMBNAIL_STORAGE = 'libs.s3_storages.ThumbRootS3BotoStorage'
# THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
# THUMBNAIL_REDIS_HOST = REDIS.hostname
# THUMBNAIL_REDIS_PORT = REDIS.port
# THUMBNAIL_REDIS_DB = 0
# THUMBNAIL_REDIS_PASSWORD = REDIS.password
# THUMBNAIL_REDIS_UNIX_SOCKET_PATH = None


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],  # "null"
            "propagate": True,
            "level": "WARNING",
        },
        "django.request": {
            "handlers": ["console"],
            "level": "WARNING",  # "ERROR"
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "propagate": False,
            "level": "WARNING",
        },

        "apps": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
    }
}
