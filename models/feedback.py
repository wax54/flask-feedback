from models import db, AbstractBDModel


class Feedback(db.Model, AbstractBDModel):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey(
        'users.username', ondelete="cascade"))

    user = db.relationship("User", backref="feedback")

    def update_from_serial(self, d):
        id = d.get('id')
        title = d.get('title')
        content = d.get('content')
        username = d.get('username')

        if id:
            self.id = id
        if title:
            self.title = title
        if content:
            self.content = content
        if username:
            self.username = username
        try:
            self.update_db()
            return True
        except:
            return False

    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'content': self.content,
                'username': self.username
                }
