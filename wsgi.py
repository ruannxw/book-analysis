import sys

WIN = sys.platform.startswith('win')
from gevent import monkey

if WIN:
    monkey.patch_all(contextvars=False)
else:
    monkey.patch_all()
# gc.disable()
# gc.set_debug(gc.DEBUG_LEAK)
import os

from dotenv import load_dotenv, find_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix

from BookAnalysis import create_app

load_dotenv(find_dotenv())

app = create_app(os.environ.get('FLASK_ENV', 'production'))
app.wsgi_app = ProxyFix(app.wsgi_app)