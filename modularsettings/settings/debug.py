def require(DEV_ENV, **kwargs):

    DEBUG = DEV_ENV
    TEMPLATE_DEBUG = DEBUG

    return locals()
