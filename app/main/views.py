from flask import render_template,redirect,url_for,request
from . import main
from .forms import PizzaForm,OrderForm
from ..models import Pizza


@main.route('/')
def index():
    pizzas = Pizza.query.filter_by().all()
    large_pizza = Pizza.query.filter_by(pizza_size = 'Large')
    small_pizza = Pizza.query.filter_by(pizza_size = 'Small')
    medium_pizza = Pizza.query.filter_by(pizza_size = 'Medium')
    title = 'Crustacean Pizza'
    return render_template('index.html', title=title,pizzas=pizzas,large_pizza=large_pizza,medium_pizza=medium_pizza,small_pizza=small_pizza)

@main.route('/menu')
def menus():
    pizzas = Pizza.query.filter_by().all()
    large_pizza = Pizza.query.filter_by(pizza_size = 'Large')
    small_pizza = Pizza.query.filter_by(pizza_size = 'Small')
    medium_pizza = Pizza.query.filter_by(pizza_size = 'Medium')
    title = 'Crustacean Pizza'
    return render_template('menu.html', title=title,pizzas=pizzas,large_pizza=large_pizza,medium_pizza=medium_pizza,small_pizza=small_pizza)



@main.route('/new_pizza', methods=['GET','POST'])
def new_pizza():
    form = PizzaForm()
    if form.validate_on_submit():
        pizza_name = form.pizza_name.data
        pizza_size = form.pizza_size.data
        pizza_price = form.pizza_price.data
        # print(form.pizza_picture_path.data)
        # pizza_picture_path.save(form.pizza_picture_path.data)
        pizza_picture_path = form.pizza_picture_path.data
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            pizza_picture_path = path
            # db.session.commit()
            
        # filename = pizza_picture_path.save(form.pizza_picture_path.data)
        new_pizza_object = Pizza(pizza_name=pizza_name,pizza_size=pizza_size,pizza_price=pizza_price,pizza_picture_path=pizza_picture_path)
        new_pizza_object.save_pizza()
        # return redirect(url_for('main.index'))
    return render_template('new_pizza.html',form = form)
        
@main.route('/checkout')
def checkout():
    return render_template('cart.html')