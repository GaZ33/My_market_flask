from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Iniciando a aplicação do Flask
app = Flask(__name__)

# Pegando o valor do da variável chamada DB_CONNECTION do .env
db_connection = os.getenv("DB_CONNECTION")
# Incuindo a path do MySQL nas config da aplicação para poder acessar o DB
app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
# Desativa o rastreamento de modificações para evitar avisos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Criando uma chave de criptografia para as senhas registradas
app.config['SECRET_KEY'] = '95f1760008984d43f87bcdec'

bcrypt = Bcrypt()

# Criando a instância do SQLAlchemy referênciando a aplicação que estamos trabalhando
db = SQLAlchemy(app)

# Comando para executar/modificar/adicionar as queries
app.app_context().push()
from market.models import Item
from market import routes


