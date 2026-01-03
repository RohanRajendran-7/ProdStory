from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from .main import main_bp
    from .auth import auth_bp
    from .upload import upload_bp
    print("Registering blueprints...")
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth') 
    app.register_blueprint(upload_bp, url_prefix='/video')

    return app
