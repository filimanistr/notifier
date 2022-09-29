from aiohttp import web
import jinja2
import aiohttp_jinja2
from aiohttp_session import get_session, setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

def setup_routes(application):
    from app.routes import setup_routes as setup_routes
    setup_routes(application)

def setup_external_libraries(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))
    app['static_root_url'] = 'static'

def setup_session_storage(app):
    from cryptography import fernet
    key = fernet.Fernet.generate_key()
    f = fernet.Fernet(key)
    # The storage that saves session data in HTTP cookies
    setup(app, EncryptedCookieStorage(f))

def setup_app(application):
    setup_session_storage(application)
    setup_external_libraries(application)
    setup_routes(application)

app = web.Application()


if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)


