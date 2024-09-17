from flask import Blueprint,render_template,redirect,url_for

auth = Blueprint('auth', __name__)

@auth.route("/")
def home():
    return "Hello !! Welcome Login Home"

@auth.route('/login')
def login():
    return "Login Page"