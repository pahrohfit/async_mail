from functools import lru_cache


@lru_cache()
def get_settings():

    try:
        from simple_settings import settings
        _ = settings.EMAIL_BACKEND
        return settings
    except (RuntimeError, ImportError, ModuleNotFoundError):
        pass
    try:
        from sanic import Sanic
        _ = Sanic.get_app().config.EMAIL_BACKEND
        return Sanic.get_app().config
    except (RuntimeError, ImportError, ModuleNotFoundError):
        pass
    try:
        from flask import flask
        _ = flask.current_app.config.EMAIL_BACKEND
        return flask.current_app.config
    except (RuntimeError, ImportError, ModuleNotFoundError):
        pass
    try:
        from django.conf import settings
        _ = settings.EMAIL_BACKEND
        return settings
    except (ModuleNotFoundError, ImportError):
        pass
    raise ImportError(
        'Could not load settings. First tried simple_settings, '
        'then django settings'
    )


settings = get_settings()
