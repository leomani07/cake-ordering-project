from app import db, Cake

db.create_all()

cakes = [
    Cake(name='Chocolate Truffle', price=450.00,
         image='https://cdn.pixabay.com/photo/2017/05/07/08/56/cake-2299966_1280.jpg',
         description='Rich chocolate sponge layered with ganache.'),
    Cake(name='Vanilla Berry', price=380.00,
         image='https://cdn.pixabay.com/photo/2016/03/05/19/02/homemade-1238600_1280.jpg',
         description='Classic vanilla flavor with fresh berries.'),
    Cake(name='Red Velvet', price=500.00,
         image='https://cdn.pixabay.com/photo/2020/06/02/17/18/red-velvet-5253543_1280.jpg',
         description='Smooth red velvet with cream cheese frosting.')
]

db.session.bulk_save_objects(cakes)
db.session.commit()
print("✅ Cake data added!")
