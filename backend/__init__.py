from flask import Flask
from flask_bcrypt import Bcrypt

# Initialize Bcrypt without app initially
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Initialize Bcrypt with the Flask app instance
    bcrypt.init_app(app)

    # Import and register blueprints here
    from .routes.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
