from .settings import *
import dj_database_url
db_from_env = dj_database_url.config(env='DATABASE_URL', conn_max_age=500)

DEBUG = False

# 기존 DATABASES
DATABASES['default'].update(db_from_env)

CACHES = {
    "default": {
         "BACKEND": "redis_cache.RedisCache",
         "LOCATION": os.environ.get('REDIS_URL'),
    }
}