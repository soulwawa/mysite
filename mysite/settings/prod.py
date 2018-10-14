from .settings import *

import dj_database_url
db_from_env = dj_database_url.config(env='DATABASE_URL', conn_max_age=500)

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',)

MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',)

# 기존 DATABASES
DATABASES['default'].update(db_from_env)