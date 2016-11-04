from citation_manager.settings.common import *

INSTALLED_APPS += ['storages']
AWS_STORAGE_BUCKET_NAME = "cm-static-files"
STATICFILES_STORAGE = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
