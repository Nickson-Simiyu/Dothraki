from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy object
db = SQLAlchemy()

# Function to initialize the database
def init_db(app):
    app.config.from_object('config.Config')  # Load config settings from a config file or class
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create tables based on models
