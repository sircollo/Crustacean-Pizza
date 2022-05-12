from flask import render_template,redirect,url_for
from . import main
from .forms import PizzaForm
from ..models import Pizza

@main.route('/')
def index():
    title = 'Crustacean Pizza'
    return render_template('index.html', title=title)


@main.route('/new_pizza', methods=['GET','POST'])
def new_pizza():
    form = PizzaForm()
    if form.validate_on_submit():
        pizza_name = form.pizza_name.data
        pizza_size = form.pizza_size.data
        pizza_price = form.pizza_price.data
        pizza_picture_path = form.pizza_picture_path.data
        
        new_pizza_object = Pizza(pizza_name=pizza_name,pizza_size=pizza_size,pizza_price=pizza_price,pizza_picture_path=pizza_picture_path)
        new_pizza_object.save_pizza()
        return redirect(url_for('main.index'))
    return render_template('new_pizza.html',form = form)
        