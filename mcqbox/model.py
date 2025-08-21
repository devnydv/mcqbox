from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
    
class Subcategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('subcategories', lazy=True))
    description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_id': self.category_id,
            'description': self.description,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    colour = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'colour': self.colour,
            'created_at': datetime.now(),
            
        }
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('tags', lazy=True))
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=True)
    subcategory = db.relationship('Subcategory', backref=db.backref('tags', lazy=True))  
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category_id': self.category_id,
            'subcategory_id': self.subcategory_id,
            'created_at': datetime.now(),
            
        }

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('subcategory.id'), nullable=False)
    subcategory = db.relationship('Subcategory', backref=db.backref('questions', lazy=True))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=True)
    tag = db.relationship('Tag', backref=db.backref('questions', lazy=True))
    explanation = db.Column(db.String(500), nullable=True)
    options = db.Column(db.JSON, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('questions', lazy=True))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())