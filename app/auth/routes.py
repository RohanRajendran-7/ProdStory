from flask import Blueprint

# The second argument is '__name__', which tells Flask where to find this blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    print("inside login route")
    return "This is the login page."

@auth_bp.route('/register')
def register():
    return "This is the register page."
