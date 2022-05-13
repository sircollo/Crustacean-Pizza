from . import db,login_manager
from app import create_app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  __tablename__='users'
  id = db.Column(db.Integer,primary_key = True)
  email = db.Column(db.String(255),unique=True,nullable=False)
  username = db.Column(db.String(255),unique=True,nullable=False)
  pass_secure = db.Column(db.String(255),nullable=True)
  
  
  @property
  def set_password(self):
    raise AttributeError('You cannot read password attr')
  
  @set_password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  
  def save_user(self):
    db.session.add(self)
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def __repr__(self):
    return f'User {self.username}'
  

class Pizza(db.Model):
  __tablename__='pizzas'
  id = db.Column(db.Integer,primary_key = True)
  pizza_name = db.Column(db.String(255),unique=True,nullable=False)
  pizza_size = db.Column(db.String(255),nullable=False)
  pizza_price = db.Column(db.Integer(),nullable=True) 
  pizza_picture_path = db.Column(db.String())
  
  
  def save_pizza(self):
    db.session.add(self)
    db.session.commit()
    
  def delete_pizza(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_pizzas(cls,pizza_size):
    pizzas = Pizza.query.filter_by(pizza_size=pizza_size).all()
    return pizzas
  
  def __repr__(self):
    return f'Pizza {self.pizza_name}'
  
class Topping(db.Model):
  __tablename__='toppings'
  id = db.Column(db.Integer,primary_key = True)
  topping_name = db.Column(db.String(255),unique=True,nullable=False)
  topping_price = db.Column(db.Integer())
 
  
  def save_topping(self):
    db.session.add(self)
    db.session.commit()
    
  def delete_topping(self):
    db.session.delete(self)
    db.session.commit()

  def get_toppings(cls,topping_name):
    toppings = Topping.query.filter_by(topping_name=topping_name).all()
    return toppings
  
  def __repr__(self):
    return f'Pizza {self.pizza_name}'
  
  
