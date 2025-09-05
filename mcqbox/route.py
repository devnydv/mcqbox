from mcqbox import app

from flask import render_template, send_from_directory

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')