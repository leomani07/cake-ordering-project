from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    address = db.Column(db.String(200))
    cake_id = db.Column(db.Integer, db.ForeignKey('cake.id'))

    cake = db.relationship('Cake', backref='orders')
