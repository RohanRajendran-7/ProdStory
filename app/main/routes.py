from flask import Blueprint, render_template

# The second argument is '__name__', which tells Flask where to find this blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')
