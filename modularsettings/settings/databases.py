import os

def require(DEV_ENV, BASE_PATH, DATABASE_USER, DATABASE_PASSWORD,
        DATABASE_HOST, DATABASE_PORT, **kwargs):

    if DEV_ENV:
        database_dir = os.path.join(BASE_PATH, 'databases')

        if not os.path.exists(database_dir):
            os.mkdir(database_dir)

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(database_dir, 'sqlite3'),
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'USER': DATABASE_USER,
                'PASSWORD': DATABASE_PASSWORD,
                'HOST': DATABASE_HOST,
                'PORT': DATABASE_PORT,
            }
        }

    return locals()
