from flask import render_template,url_for,redirect,request,flash
from flask_login import login_user
from . import auth
from ..models import User,Pizza,Topping
from ..import db


@auth.route('/admin')
def login():
    pass