from flask import  request,render_template, redirect, url_for
from app.models import Product,Category, db
# connect blueprint with views
from app.products import product_blueprint
import os



@product_blueprint.route('/contact', endpoint='contact_us')
def contact_us():
    return  render_template('landing/contact_us.html')

@product_blueprint.route('/about', endpoint='about_us')
def about_us():
    return  render_template('landing/about_us.html')

        
        
        
@product_blueprint.route('/', endpoint='products_index')
def students_index():
    products = Product.query.all()
    return  render_template('product/index.html', products=products)

@product_blueprint.route('/products/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)

    if product:
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('products.products_index'))

    return redirect(url_for('products.products_index'))


@product_blueprint.route('/create_product', methods=['GET', 'POST'],endpoint='products_create')
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.files['image']
        in_stock = bool(request.form.get('in_stock'))
        category_id = request.form['category'] 



        if image:
            upload_folder = 'static/uploads' 
            if not os.path.exists(upload_folder):
                 os.makedirs(upload_folder)

            image_path = os.path.join(upload_folder,image.filename)
            image.save(image_path)

        new_product = Product(
            name=name,
            description=description,
            price=price,
            image=image_path,
            in_stock=in_stock,
            category_id = category_id  # Get the selected category ID
 
            
        )

        db.session.add(new_product)
        db.session.commit()

        return redirect('/') 
    
    categories=Category.query.all()

    return render_template('product/create_product.html', categories=categories)
        
        
@product_blueprint.route('/products/<int:product_id>/edit', methods=['GET', 'POST'], endpoint='products_edit')
def edit_product(product_id):
    product = Product.query.get(product_id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = request.form['price']


        category_id = request.form['category']  # Get the selected category ID
        product.category_id = category_id 
        
        image = request.files['image']
        if image:
            upload_folder = 'static/uploads'  
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)

            product.image = image_path

        db.session.commit()
        return redirect(url_for('products.products_index'))

    categories = Category.query.all()
    return render_template('product/edit_product.html', product=product, categories=categories)


@product_blueprint.route('/products/<int:product_id>', endpoint='products_details')
def product_details(product_id):
    product = Product.query.get(product_id)
    return render_template('product/product_details.html', product=product)


@product_blueprint.route('/products/by_category/<int:category_id>', endpoint='products_by_category')
def products_by_category(category_id):
    products = Product.query.filter_by(category_id=category_id).all()
    return render_template('product/products_by_category.html', products=products)

