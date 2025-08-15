from mcqbox import app
from flask import Flask, render_template



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/category/<category>")
def category(category):
    print(category)
    return render_template("cate.html")    
@app.route("/category/<category>/<topic>/<id>")
def mcq(category, topic, id):
    print(category)
    return render_template("mcq.html")  




