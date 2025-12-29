from extensions import db

class Cake(db.Model):
    __tablename__ = "cake"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200))
    description = db.Column(db.String(300))


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(300), nullable=False)
    cake_id = db.Column(db.Integer, db.ForeignKey("cake.id"), nullable=False)

