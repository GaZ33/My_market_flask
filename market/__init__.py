from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Pegando o valor do .env
db_connection = os.getenv("DB_CONNECTION")

app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
# Desativa o rastreamento de modificações para evitar avisos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
from market.models import Item
from market import routes


