from mcqbox import app
from flask import Flask, render_template
from mcqbox.model import db, Category, Subcategory, Question


@app.route("/")
def home():
    category = Category.query.all()
    
    return render_template("index.html", category = category)

@app.route("/category/<category_name>")
def category(category_name):
    category_name = category_name.replace('-', ' ')
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        return {"error": "Category not found"}, 404

    # Access subcategories via backref
    subcategories = category.subcategories

    
    
    return render_template("cate.html", cat = category_name, subcategories=subcategories)    
@app.route("/category/<category>/<topic>/<id>")
def mcq(category, topic, id):
    print(category)
    return render_template("mcq.html")  




