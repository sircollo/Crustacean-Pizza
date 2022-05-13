from flask import render_template
from . import main


@main.route('/')
def index():
    title = 'Crustacean Pizza'
    return render_template('index.html', title=title)


@main.route('/about')
def about():
    title = 'Crustacean Pizza'
    return render_template('about.html', title=title)    