from sre_parse import CATEGORIES
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField,IntegerField
from wtforms.validators import DataRequired

SIZES = [('Large','Large'),('Medium','Medium'),('Small','Small')]

class PizzaForm(FlaskForm):
  pizza_name = StringField('Pizza Name',validators=[DataRequired()])
  pizza_size = SelectField('Pizza Size',choices=SIZES,validators=[DataRequired()])
  pizza_price = IntegerField('Pizza Price',validators=[DataRequired()])
  pizza_picture_path = StringField('Picture', validators=[DataRequired()])
  submit = SubmitField('Post')