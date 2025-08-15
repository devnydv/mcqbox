from flask import Blueprint

backend = Blueprint("backend_", __name__, static_folder='static', static_url_path='/backend_/static', template_folder='templates', url_prefix='/backend')

from mcqbox.backend import route
