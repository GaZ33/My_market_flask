from market import db


class Item(db.Model):
    IdItem = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    Description = db.Column(db.String(length=1024))
    Quantity = db.Column(db.Integer())
    Barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    #User_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Item {self.Name}"