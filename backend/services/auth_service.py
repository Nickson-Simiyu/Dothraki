from models import User

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return {'message':'Login Successful'}, 200
    return {'message': 'Invalid Credentials'}, 401