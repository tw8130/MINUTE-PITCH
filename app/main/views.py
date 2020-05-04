from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required,current_user
from ..models import User

@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Home - Welcome to The Pitch website'

    return render_template('index.html', title=title)