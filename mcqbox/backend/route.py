from mcqbox import app

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#from data_store import DataStore
from mcqbox.model import db, Category, Subcategory, Question, Tags, Tag

# Configure logging


#app = Flask(__name__)
# app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")




#data_store = DataStore()

@app.route('/backend')
def dashboard():
    """Dashboard with statistics and overview"""
    categories = Category.query.count()
    subcategories = Subcategory.query.count()
    questions = Question.query.count()
    category_stats = {}
    subcategory_stats = {}
    category = Category.query.all()
    subcat = Subcategory.query.all()   
    for cat in category:
        category_stats[cat.id] = {
            'id': cat.id,
            'name': cat.name,
            'total_subcategories': len(cat.subcategories),
            'count': len(cat.questions)
        }

    for subcategory in subcat:
        subcategory_stats[subcategory.id] = {
            'id': subcategory.id,
            'name': subcategory.name,
            'category_id': subcategory.category_id,
            'count': len(subcategory.questions)
        }

    # Prepare data for rendering
    stats ={
            'total_categories': categories,
            'total_subcategories': subcategories,
            'total_questions': questions,
            'category_stats': list(category_stats.values()),
            'subcategory_stats': list(subcategory_stats.values())
        }
    #stats = data_store.get_statistics()
    #categories = data_store.get_all_categories()
    return render_template('dashboard.html', stats=stats, categories=category)
#done
@app.route('/backend/categories')
def categories():
    """Categories management page"""
    categories_list = Category.query.all()
    #categories_list = data_store.get_all_categories()
    return render_template('categories.html', categories=categories_list)
#done
@app.route('/backend/categories/create', methods=['POST'])
def create_category():
    """Create new category"""
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    

    if not name:
        flash('Category name is required', 'error')
        return redirect(url_for('categories'))
    #insert to sqldb
    category = Category(
        name= name,
        description= description
    )
    try:
        db.session.add(category)
        db.session.commit()
    
        
        #data_store.create_category(name, description)
        flash('Category created successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(f'Error creating category: {str(e)}', 'error')
        flash(str(e), 'error')
    
    return redirect(url_for('categories'))

#done
@app.route('/backend/categories/<int:category_id>/edit', methods=['POST'])
def edit_category(category_id):
    """Edit existing category"""
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    
    if not name:
        flash('Category name is required', 'error')
        return redirect(url_for('categories'))
    

    try:
        category = Category.query.get(category_id)
        category.name = name
        category.description = description
        db.session.commit()
        #data_store.update_category(category_id, name, description)
        flash('Category updated successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('categories'))
#done
@app.route('/backend/categories/<int:category_id>/delete', methods=['POST'])
def delete_category(category_id):
    """Delete category"""
    try:
        category = Category.query.get(category_id)
        db.session.delete(category)
        db.session.commit()
        #data_store.delete_category(category_id)
        flash('Category deleted successfully', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('categories'))

@app.route('/backend/subcategories')
def subcategories():
    """Subcategories management page"""
    # category_id = Category.query.get('category_id')
    category_id = request.args.get('category_id', type=int)
    
    categories_list = Category.query.all()
    #categories_list = data_store.get_all_categories()
    
    if category_id:
        subcategories_list = Subcategory.query.filter_by(category_id=category_id).all()
        #subcategories_list = data_store.get_subcategories_by_category(category_id)
        selected_category = Category.query.get(category_id)
        #selected_category = data_store.get_category(category_id)
    else:
        subcategories_list = Subcategory.query.all()
        selected_category = None
    
    return render_template('subcategories.html', 
                         subcategories=subcategories_list, 
                         categories=categories_list,
                         selected_category=selected_category)
#done
@app.route('/backend/subcategories/create', methods=['POST'])
def create_subcategory():
    """Create new subcategory"""
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    category_id = request.form.get('category_id', type=int)
    print(name, description, category_id)
    if not name:
        flash('Subcategory name is required', 'error')
        return redirect(url_for('subcategories'))
    
    if not category_id:
        flash('Category is required', 'error')
        return redirect(url_for('subcategories'))
    
    try:
        subcategories = Subcategory(
            name=name,
            description=description,
            category_id=category_id
        )
        db.session.add(subcategories)
        db.session.commit()
        #data_store.create_subcategory(name, description, category_id)
        flash('Subcategory created successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('subcategories'))
#done
@app.route('/backend/subcategories/<int:subcategory_id>/edit', methods=['POST'])
def edit_subcategory(subcategory_id):
    """Edit existing subcategory"""
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    category_id = request.form.get('category_id', type=int)
    
    if not name:
        flash('Subcategory name is required', 'error')
        return redirect(url_for('subcategories'))
    
    if not category_id:
        flash('Category is required', 'error')
        return redirect(url_for('subcategories'))
    
    try:
        subcategory = Subcategory.query.get(subcategory_id)
        subcategory.name = name
        subcategory.description = description
        subcategory.category_id = category_id
        db.session.commit()
        #data_store.update_subcategory(subcategory_id, name, description, category_id)
        flash('Subcategory updated successfully', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('subcategories'))

#done
@app.route('/backend/subcategories/<int:subcategory_id>/delete', methods=['POST'])
def delete_subcategory(subcategory_id):
    """Delete subcategory"""
    try:
        subcategory = Subcategory.query.get(subcategory_id)
        db.session.delete(subcategory)
        db.session.commit()
        #data_store.delete_subcategory(subcategory_id)
        flash('Subcategory deleted successfully', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('subcategories'))

@app.route('/api/tags')
def api_tags():
    """API endpoint to get all tags"""
    tags = Tags.query.all()
    #tags = data_store.get_all_tags()
    return jsonify({
            'id': tags.id,
            'name': tags.name,
            'colour': tags.colour
        })
#done
@app.route('/backend/tags')
def tags():
    """Tags management page"""
    category_id = request.args.get('category_id', type=int)
    subcategory_id = request.args.get('subcategory_id', type=int)
    categories = Category.query.all()


    if category_id:
        subcategories_list = Subcategory.query.filter_by(category_id=category_id).all()
        tag = Tag.query.filter_by(category_id=category_id, subcategory_id= subcategory_id).all()
    else:
        tag = Tag.query.all()
        subcategories_list = []
    #tags_list = data_store.get_all_tags()
    return render_template('tags.html', 
                            tags = tag,
                           categories=categories,
                           selected_category=category_id,
                            selected_subcategory=subcategory_id,
                             subcategories=subcategories_list
                           )

@app.route('/backend/tags/create', methods=['POST'])
def create_tag():
    """Create new tag"""
    name = request.form.get('name', '').strip()
    subcategory_id = request.form.get('subcategory_id', type=int)
    category_id = request.form.get('category_id', type=int)
    
    if not name:
        flash('Tag name is required', 'error')
        return redirect(url_for('tags'))
    
    try:
        tag = Tag(
            name=name,
            subcategory_id=subcategory_id,
            category_id=category_id,
            #color=color
            
        )
        db.session.add(tag)
        db.session.commit()
        #data_store.create_tag(name, color)
        flash('Tag created successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('tags'))


@app.route('/backend/tags/<int:tag_id>/edit', methods=['POST'])
def edit_tag(tag_id):
    """Edit existing subcategory"""
    name = request.form.get('name', '').strip()
    subcategory_id = request.form.get('subcategory_id', type=int)
    category_id = request.form.get('category_id', type=int)
    
    if not name:
        flash('Subcategory name is required', 'error')
        return redirect(url_for('tags'))
    
    if not category_id:
        flash('Category is required', 'error')
        return redirect(url_for('tags'))
    if not subcategory_id:
        flash('Category is required', 'error')
        return redirect(url_for('tags'))
    try:
        tag = Tag.query.get(tag_id)
        tag.subcategory_id = subcategory_id
        tag.category_id = category_id
        db.session.commit()
        #data_store.update_subcategory(subcategory_id, name, description, category_id)
        flash('Subcategory updated successfully', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('tags'))


@app.route('/backend/tags/<tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    """Delete tag"""
    
    try:
        tag = Tag.query.filter_by(id=tag_id).first()
        if not tag:
            flash('Tag not found', 'error')
            return redirect(url_for('tags'))
        
        db.session.delete(tag)
        db.session.commit()
        #data_store.delete_tag(tag_name)
        flash('Tag deleted successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('tags'))


#done
@app.route('/backend/questions')
def questions():
    """Questions management page"""
    category_id = request.args.get('category_id', type=int)
    subcategory_id = request.args.get('subcategory_id', type=int)
    search = request.args.get('search', '').strip()
    tag_filter = request.args.get('tag', '').strip()
    categories_list = Category.query.all()
    subcategories_list = []
    tags_list = Tag.query.all()
    if category_id:
        subcategories_list = Subcategory.query.filter_by(category_id=category_id).all()
        
        #subcategories_list = data_store.get_subcategories_by_category(category_id)
    # Build filters dynamically
    filters = []
    if category_id:
        filters.append(Question.category_id == category_id)
    if subcategory_id:
        filters.append(Question.subcategory_id == subcategory_id)
    tag_filter = request.args.get('tag', '').strip()
    if tag_filter:
        filters.append(Question.tag_id == tag_filter)
    if search:
        filters.append(Question.question_text.ilike(f'%{search}%'))
    
    # Apply filters only if they exist
    questions_list = Question.query.filter(*filters).all()
    for question in questions_list:
        print(question.subcategory.name)
    #questions_list = data_store.get_questions_filtered(category_id, subcategory_id, search)
    
    return render_template('questions.html', 
                         questions=questions_list, 
                         categories=categories_list,
                         subcategories=subcategories_list,
                         tags=tags_list,
                         selected_category=category_id,
                         selected_subcategory=subcategory_id,
                         search_query=search)
#done
@app.route('/backend/questions/create', methods=['POST'])
def create_question():
    """Create new question"""
    question_text = request.form.get('question_text', '').strip()
    subcategory_id = request.form.get('subcategory_id', type=int)
    category_id = request.form.get('category_id', type=int)
    explanation = request.form.get('explanation', '').strip()
    tags_id = request.form.get('tags', type= int)
    if not explanation:
        explanation = None
    options = []
    
    correct_option = request.form.get('correct_option', type=int)
    
    
    
    

    # Get all options
    for i in range(1, 5):  # Assuming max 4 options
        option_text = request.form.get(f'option_{i}', '').strip()
        if option_text:
            options.append({
                'text': option_text,
                'is_correct': (i == correct_option)
            })
    
    if not question_text:
        flash('Question text is required', 'error')
        return redirect(url_for('questions'))
    
    if not subcategory_id:
        flash('Subcategory is required', 'error')
        return redirect(url_for('questions'))
    
    if len(options) < 2:
        flash('At least 2 options are required', 'error')
        return redirect(url_for('questions'))
    
    if not any(opt['is_correct'] for opt in options):
        flash('At least one correct option must be selected', 'error')
        return redirect(url_for('questions'))
    
    try:
        question = Question(
            question_text=question_text,
            subcategory_id=subcategory_id,
            category_id= category_id,
            options=options,
            explanation=explanation,
            tag_id=tags_id
        )
        db.session.add(question)
        db.session.commit()
        #data_store.create_question(question_text, subcategory_id, options, category_id)
        flash('Question created successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('questions'))
#done
@app.route('/backend/questions/<int:question_id>/edit', methods=['POST'])
def edit_question(question_id):
    """Edit existing question"""
    question_text = request.form.get('question_text', '').strip()
    subcategory_id = request.form.get('subcategory_id', type=int)
    tags_id = request.form.get('tags', type=int)
    category_id = request.form.get('category_id', type=int)
    #explanation = request.form.get('explanation', '').strip()
    options = []
    correct_option = request.form.get('correct_option', type=int)
    
    # Get all options
    for i in range(1, 5):  # Assuming max 4 options
        option_text = request.form.get(f'option_{i}', '').strip()
        if option_text:
            options.append({
                'text': option_text,
                'is_correct': (i == correct_option)
            })
    
    if not question_text:
        flash('Question text is required', 'error')
        return redirect(url_for('questions'))
    
    if not subcategory_id:
        flash('Subcategory is required', 'error')
        return redirect(url_for('questions'))
    
    if len(options) < 2:
        flash('At least 2 options are required', 'error')
        return redirect(url_for('questions'))
    
    if not any(opt['is_correct'] for opt in options):
        flash('At least one correct option must be selected', 'error')
        return redirect(url_for('questions'))
    
    try:
        question = Question.query.get(question_id)
        question.question_text = question_text
        question.subcategory_id = subcategory_id
        question.options = options
        question.category_id = category_id
        question.tag = tags_id
        db.session.commit()
        #data_store.update_question(question_id, question_text, subcategory_id, options)
        flash('Question updated successfully', 'success')
    except ValueError as e:
        db.session.rollback()
        flash(str(e), 'error')
    
    return redirect(url_for('questions'))
#done
@app.route('/backend/questions/<int:question_id>/delete', methods=['POST'])
def delete_question(question_id):
    """Delete question"""
    try:
        question = Question.query.get(question_id)
        db.session.delete(question)
        db.session.commit()
        #data_store.delete_question(question_id)
        flash('Question deleted successfully', 'success')
    except ValueError as e:
        flash(str(e), 'error')
    
    return redirect(url_for('questions'))
#done
@app.route('/api/subcategories/<int:category_id>')
def api_subcategories(category_id):
    """API endpoint to get subcategories by category"""
    subcategories = Subcategory.query.filter_by(category_id=category_id).all()
    #subcategories = data_store.get_subcategories_by_category(category_id)
    return jsonify([{
        'id': sub.id,
        'name': sub.name
    } for sub in subcategories])
#done
@app.route('/api/category/<int:category_id>')
def api_category(category_id):
    """API endpoint to get category details"""
    try:
        category = Category.query.get(category_id)
        #category = data_store.get_category(category_id)
        return jsonify({
            'id': category.id,
            'name': category.name,
            'description': category.description,
            
        })
    except ValueError:
        return jsonify({'error': 'Category not found'}), 404
#done
@app.route('/api/subcategory/<int:subcategory_id>')
def api_subcategory(subcategory_id):
    """API endpoint to get subcategory details"""
    try:
        subcategory = Subcategory.query.get(subcategory_id)
        #subcategory = data_store.get_subcategory(subcategory_id)
        return jsonify({
            'id': subcategory.id,
            'name': subcategory.name,
            'category_id': subcategory.category_id,
            'description': subcategory.description,
            
        })
    except ValueError:
        return jsonify({'error': 'Subcategory not found'}), 404
#done
@app.route('/api/question/<int:question_id>')
def api_question(question_id):
    """API endpoint to get question details"""
    try:
        question = Question.query.get(question_id)
        #question = data_store.get_question(question_id)
        return jsonify({
        'id': question.id,
        'category_id': question.category.name,
        'subcategory_id': question.subcategory.name,
        'question_text': question.question_text,
        'options': question.options,
        'explanation': question.explanation,
        "tag_id": question.tag.name,
    })
    except ValueError:
        return jsonify({'error': 'Question not found'}), 404
