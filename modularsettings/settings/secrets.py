import env


# Make this unique, and don't share it with anybody.
SECRET_KEY = '000000000000000000000000000000000000000000000000000000'

if env.TEST_ENV:
    DATABASE_USER = 'test user'
    DATABASE_PASSWORD = 'test password'
elif env.PROD_ENV:
    DATABASE_USER = 'prod user'
    DATABASE_PASSWORD = 'prod password'

DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
