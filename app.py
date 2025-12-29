from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cakes.db'
db = SQLAlchemy(app)

class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image = db.Column(db.String(200))
    description = db.Column(db.String(300))

@app.route('/')
def index():
    cakes = Cake.query.all()
    return render_template('index.html', cakes=cakes)

@app.route('/order/<int:cake_id>', methods=['GET', 'POST'])
def order(cake_id):
    cake = Cake.query.get_or_404(cake_id)
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        new_order = Order(customer_name=name, phone=phone, address=address, cake_id=cake.id)
        db.session.add(new_order)
        db.session.commit()
        return f"<h2>Thanks for ordering {cake.name}!</h2>"
    return render_template('order.html', cake=cake)
