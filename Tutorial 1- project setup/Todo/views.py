from flask import Blueprint,render_template,redirect,url_for


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "Hello !! Welcome Home"

@views.route('/login')
def login():
    return "Login Page"