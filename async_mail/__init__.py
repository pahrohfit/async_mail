from async_mail.backends import get_backend

#Mail = get_backend()
Mail: object = ()

class Mail:

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)


    def init_app(self, app = None):
        _backend = get_backend()
        self = _backend

        return _backend