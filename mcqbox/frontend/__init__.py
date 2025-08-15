from flask import Blueprint

frontend = Blueprint("frontend", __name__, template_folder='templates', static_folder='static', static_url_path='/frontend/static', url_prefix='/frontend')

from mcqbox.frontend import route