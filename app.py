from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import Cake, Order

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    cakes = Cake.query.all()
    return render_template("index.html", cakes=cakes)

@app.route("/order/<int:cake_id>", methods=["GET", "POST"])
def order(cake_id):
    cake = Cake.query.get_or_404(cake_id)

    if request.method == "POST":
        order = Order(
            customer_name=request.form["name"],
            phone=request.form["phone"],
            address=request.form["address"],
            cake_id=cake.id
        )
        db.session.add(order)
        db.session.commit()
        return f"<h2 style='text-align:center;color:#ff4081'>🎂 Thanks for ordering {cake.name}!</h2>"

    return render_template("order.html", cake=cake)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        if Cake.query.count() == 0:
            db.session.add_all([
                Cake(
                    name="Chocolate Cake",
                    price=499,
                    image="chocolate.jpg",
                    description="Rich and creamy chocolate cake"
                ),
                Cake(
                    name="Vanilla Cake",
                    price=399,
                    image="vanilla.jpg",
                    description="Soft vanilla sponge with cream"
                ),
                Cake(
                    name="Strawberry Cake",
                    price=459,
                    image="strawberry.jpg",
                    description="Fresh strawberry delight"
                )
            ])
            db.session.commit()

    app.run(host="0.0.0.0", port=80, debug=True)

