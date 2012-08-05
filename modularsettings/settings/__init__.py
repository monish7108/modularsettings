import os

from secrets import *

SETTINGS_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH  = os.path.dirname(SETTINGS_PATH)
BASE_PATH     = os.path.dirname(PROJECT_PATH)

ENV      = os.getenv('DJANGO_ENVIRONMENT', 'development')
DEV_ENV  = ENV == 'development'
TEST_ENV = ENV == 'staging'
PROD_ENV = ENV == 'production'


def _constants(d):
    return dict((key, val) for key, val in d.items() if key.isupper())

for settings_file in [filename.rstrip('.py') for filename in os.listdir(SETTINGS_PATH)
        if not filename.endswith('.pyc') and filename not in ('__init__.py', 'secrets.py')]:

    module = __import__(settings_file, globals(), locals(), [])
    settings = module.require(**_constants(locals()))
    locals().update(_constants(settings))
