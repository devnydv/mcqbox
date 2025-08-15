from mcqbox import app

from flask import render_template

@app.route('/lol')
def index():
    return 'lol'