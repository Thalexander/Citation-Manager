from citation_manager.settings.common import *

INSTALLED_APPS += ['storages']
AWS_STORAGE_BUCKET_NAME = "cm-static-files"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'BananaNutMuffins;',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
