from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from jinja2 import ChoiceLoader, FileSystemLoader
from backend.config import Config
from backend.routes.auth import auth_blueprint
from backend.models.models import db, User

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
app.jinja_loader = ChoiceLoader([
    FileSystemLoader('../backend/frontend')
])

from backend.routes.routes import main
app.register_blueprint(main)


app.register_blueprint(auth_blueprint, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
