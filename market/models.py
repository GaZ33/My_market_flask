from market import db
from market import bcrypt

# Criando a instância de Item no DB com os atributos
class Item(db.Model):
    IdItem = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(length=30), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    Description = db.Column(db.String(length=1024))
    Quantity = db.Column(db.Integer())
    Barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    Subtitle = db.Column(db.String(length=17))
    Category = db.Column(db.String(length=50))
    # Atributo especial, é a foreign key para relacionar com a tabela User
    User_id = db.Column(db.Integer(), db.ForeignKey('user.IdUser'))
    # Método para quando se criar uma instância de Item ficar com o nome e não a localização da instância
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

    # Criando uma propriedade para fazer a hash password, ela será executada como método
    @property
    def password(self):
        return self.passowrd
    # Quando atribuirem um valor a variável password ela executará o esse decorator que codificará a senha
    @password.setter
    def password(self, password_text):
        self.Password_hash = bcrypt.generate_password_hash(password_text).decode('utf-8')

    
