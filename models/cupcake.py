from models import db, AbstractBDModel


class Cupcake(db.Model, AbstractBDModel):
    __tablename__ = 'cupcakes'

    DEFAULT_IMAGE_URL = 'https://tinyurl.com/demo-cupcake'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, server_default=DEFAULT_IMAGE_URL)

    def update_from_serial(self, d):
        flavor = d.get('flavor')
        size = d.get('size')
        rating = d.get('rating')
        image = d.get('image')

        if not image:
            image = None

        if image:
            self.image = image
        if flavor:
            self.flavor = flavor
        if size:
            self.size = size
        if rating:
            self.rating = rating
        try:
            self.update_db()
            return True
        except:
            return False

    def serialize(self):
        return {'id': self.id,
                'flavor': self.flavor,
                'size': self.size,
                'rating': self.rating,
                'image': self.image
                }

    def from_serial(self, d):
        flavor = d.get('flavor')
        size = d.get('size')
        rating = d.get('rating')

        if flavor and size and rating:
            return self.update_from_serial(d)
        else:
            return False

    @classmethod
    def search_by_flavor(cls, term):
        return cls.search_by_attr('flavor', term)
