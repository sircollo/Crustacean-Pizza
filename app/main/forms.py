from sre_parse import CATEGORIES
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField,IntegerField,FileField
from wtforms.validators import DataRequired

SIZES = [('Large','Large'),('Medium','Medium'),('Small','Small')]
TOPPINGS = [('Mushroom','Mushroom'),('Beef','Beef'),('Chicken','Chicken')]
class PizzaForm(FlaskForm):
  pizza_name = StringField('Pizza Name',validators=[DataRequired()])
  pizza_size = SelectField('Pizza Size',choices=SIZES,validators=[DataRequired()])
  pizza_price = IntegerField('Pizza Price',validators=[DataRequired()])
  pizza_picture_path = FileField('Picture', validators=[DataRequired()])
  submit = SubmitField('Post')
  
class OrderForm(FlaskForm):
  pizza_name = StringField('Name',validators=[DataRequired()])
  pizza_size = SelectField('Size',choices=SIZES,validators=[DataRequired()])
  topping_name = SelectField('Topping',choices=TOPPINGS,validators=[DataRequired()])
  
  submit = SubmitField('Post')