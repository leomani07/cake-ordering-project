from app import app
from extensions import db
from models import Cake

with app.app_context():
    db.create_all()

    # Clear old cakes
    Cake.query.delete()

    cakes = [
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
            description="Fresh strawberry heart cake"
        )
    ]

    db.session.add_all(cakes)
    db.session.commit()

    print("Cakes added successfully")

