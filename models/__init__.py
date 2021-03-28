"""Database Setup"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    """Initiates a connection to the DB"""
    db.app = app
    db.init_app(app)
    db.create_all()


class AbstractBDModel():

    def update_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def delete_by_id(cls, user_id):
        cls.query.filter_by(id=user_id).delete()
        db.session.commit()

    @classmethod
    def get(cls, u_id):
        return cls.query.get_or_404(u_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def search_by_attr(cls, attr_name, term):
        attr = getattr(cls, attr_name)
        if attr:
            return cls.query.filter(attr.ilike(f'%{term}%')).all()
        else:
            return False
