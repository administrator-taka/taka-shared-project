from .base import *

DATABASES['default'].update({
    'HOST': 'db',  # Docker 内の PostgreSQL サービスの名前
})
ALLOWED_HOSTS = ['host.docker.internal']
