from flask import  request,render_template, redirect, url_for
from app.models import Category, db
# connect blueprint with views
from app.category import category_blueprint


@category_blueprint.route('/category', methods=['GET'])
def list_categories():
    categories = Category.query.all()
    return render_template('category/list.html', categories=categories)


@category_blueprint.route('/category/new', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category.list_categories'))
    return render_template('category/create.html')

@category_blueprint.route('/category/<int:category_id>/delete', methods=['POST'], endpoint='category_delete')
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
    return redirect(url_for('category.list_categories'))
