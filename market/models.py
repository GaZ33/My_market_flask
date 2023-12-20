from market import db


class Item(db.Model):
    IdItem = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    Description = db.Column(db.String(length=1024))
    Quantity = db.Column(db.Integer())
    Barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    Subtitle = db.Column(db.String(length=17))
    Category = db.Column(db.String(length=50))
    User_id = db.Column(db.Integer(), db.ForeignKey('user.IdUser'))

    def __repr__(self):
        return f"Item {self.Name}"
    
class User(db.Model):
    IdUser = db.Column(db.Integer(), primary_key=True)
    Login = db.Column(db.String(length=15), nullable=False, unique=True)
    Email = db.Column(db.String(length=50), nullable=False, unique=True)
    Password_hash = db.Column(db.String(length=60), nullable=False)
    FName = db.Column(db.String(length=15), nullable=False)
    MName = db.Column(db.String(length=25), nullable=True)
    LName = db.Column(db.String(length=15), nullable=False)
    Budget = db.Column(db.Float(), nullable=False, default=3000)
    # Criando a relação com a entidade Item
    item = db.relationship('Item', backref="Owned_user", lazy=True)
