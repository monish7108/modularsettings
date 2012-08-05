import os

def require(DEV_ENV, BASE_PATH, **kwargs):

    if DEV_ENV:
        # Absolute filesystem path to the directory that will hold user-uploaded files.
        # Example: "/home/media/media.lawrence.com/media/"
        MEDIA_ROOT = os.path.join(BASE_PATH, 'media')
    else:
        MEDIA_ROOT = '/var/www/modularsettings/media'

    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = '/media/'

    if DEV_ENV:
        # Absolute path to the directory static files should be collected to.
        # Don't put anything in this directory yourself; store your static files
        # in apps' "static/" subdirectories and in STATICFILES_DIRS.
        # Example: "/home/media/media.lawrence.com/static/"
        STATIC_ROOT = os.path.join(BASE_PATH, 'static')
    else:
        STATIC_ROOT = '/var/www/modularsettings/static'

    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = '/static/'

    # Additional locations of static files
    STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
    )

    # List of finder classes that know how to find static files in
    # various locations.
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

    return locals()
