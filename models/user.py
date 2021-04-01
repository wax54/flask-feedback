from models import db, AbstractBDModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model, AbstractBDModel):
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    @classmethod
    def register(cls, username, email, password, first_name, last_name):
        new_user = User()
        new_user.password = hash_pass(password)
        new_user.username = username
        new_user.email = email
        new_user.first_name = first_name
        new_user.last_name = last_name

        try:
            new_user.update_db()
            return new_user
        except:
            db.session.rollback()
            errors = User.get_unique_violations(username=username, email=email)
            raise InputNotUniqueError(errors)

    @classmethod
    def authenticate(cls, username, password):
        user = cls.query.get(username)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

    @classmethod
    def get_unique_violations(cls, username, email):
        errors = []
        if cls.query.filter_by(username=username).count():
            errors.append("username")
        if cls.query.filter_by(email=email).count():
            errors.append("email")
        return errors

    def update_from_serial(self, d):
        username = d.get('username')
        email = d.get('email')
        first_name = d.get('first_name')
        last_name = d.get('last_name')

        if username:
            self.username = username
        if email:
            self.email = email
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        try:
            self.update_db()
            return True
        except:
            return False

    def serialize(self):
        return {'username': self.username,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name
                }


def hash_pass(pwd):
    phash = bcrypt.generate_password_hash(pwd)
    return phash.decode('utf8')


new_user = {"username": "johnny", "password": "blanket",
            "first_name": "Johnny", "last_name": "Test", "email": "123good@gmail.com"}


class InputNotUniqueError(Exception):
    """Exception raised for IntegrityError, but with more usable details.

    Attributes:
        invalid_columns -- an array containing the string name of 
            columns with invalid inputs
        message -- explanation of the error
    """

    def __init__(self, errors, message="Duplicates found for columns "):
        self.errors = errors
        message += "[ "
        for e in errors:
            message += f' "{e}" '
        message += " ]"
        self.message = message
        super().__init__(self.message)
