DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'krovlya_db',
    'USER': 'krovlya_admin',
    'PASSWORD': 'ni2nana7roku6',
    'HOST': 'localhost'
  }
}