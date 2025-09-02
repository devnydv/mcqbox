from mcqbox import app
from flask import Flask, render_template, request
from mcqbox.model import db, Category, Subcategory, Question, Tag


@app.route("/")
def home():
    category = Category.query.all()
    return render_template("index.html", category = category)

@app.route("/category")
def category():
    category = Category.query.all()
    return render_template("category.html" , category=category)

@app.route("/category/<category_name>")
def subcategory(category_name):
    category_name = category_name.replace('-', ' ')
    category = Category.query.filter_by(name=category_name).first()
    if not category:
        return {"error": "Category not found"}, 404

    # Access subcategories via backref
    subcategories = category.subcategories if category else []
    if not subcategories:
        return render_template("subcate.html", cat = category_name, subcategories=None)
    
    # pass tag  for so that it remains selected in mcq page
    
    return render_template("subcate.html", cat = category_name, subcategories=subcategories)    
@app.route("/category/<category>/<subcat>")
def mcq(category, subcat):
    #handle category section
    category = category.replace('-', ' ')
    category_db = Category.query.filter_by(name=category).first()
    cate_id = category_db.id

    # handle subcategory section
    subcat = subcat.replace('-', ' ')
    subcategory_id = Subcategory.query.filter_by(name=subcat, category_id=cate_id).first()
    subcat_id = subcategory_id.id if subcategory_id else None
    #question = Question.query.filter_by(subcategory_id=subcat_id).all()
    # limit to 50 questions only to make page load faster
    #question = Question.query.filter_by(subcategory_id=subcat_id).limit(50).all()

    # handle tag section 
    tag = request.args.get("tag")
    if tag:
        tag = tag.replace('-', ' ')
        question = Question.query.join(Tag).filter(Tag.name == tag).all()
    else:
        tag = Tag.query.filter_by(subcategory_id=subcat_id).first()
        tag = tag.name if tag else None
        question = Question.query.join(Tag).filter(Tag.name == tag).all()
    #question = question[0] if question else None
    
    #get tag list 
    tags = Tag.query.filter_by(subcategory_id=subcat_id).all()
    #print
    return render_template("mcq.html" , questions=question, category=category, subcat=subcat, id=id, tags=tags, tag = tag)  

@app.route("/error")
def erroe():
    return render_template("ondev.html")


import json
   


@app.route('/lol')
def script():
    def import_questions_from_json(json_file):
        """Read a JSON file and insert questions into the database"""
        with open(json_file, "r", encoding="utf-8") as f:
            questions = json.load(f)

        for q in questions:
            question = Question(
                question_text=q["question_text"],
                subcategory_id=q["subcategory_id"],
                tag_id=q.get("tag_id"),  # can be None
                explanation=q.get("explanation"),
                options=q["options"],  # JSON column accepts dict/list
                category_id=q["category_id"]
            )
            db.session.add(question)

        db.session.commit()
        print(f"✅ Imported {len(questions)} questions successfully!")



    import_questions_from_json("questions.json")
    return 'lol'