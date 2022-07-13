from async_mail.backends import get_backend

#Mail = get_backend()
Mail = None

def init_app(app = None):
    if app:
        Mail = get_backend()

    return Mail