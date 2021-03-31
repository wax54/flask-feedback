from models import db, AbstractBDModel
from flask_bcrypt import Bcrypt


class User(db.Model, AbstractBDModel):
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    def update_from_serial(self, d):
        username = d.get('username')
        email = d.get('email')
        password = d.get('password')
        first_name = d.get('first_name')
        last_name = d.get('last_name')

        if username:
            self.username = username
        if email:
            self.email = email
        if password:
            bcrypt = Bcrypt()
            phash = bcrypt.generate_password_hash(password)
            self.password = phash
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
