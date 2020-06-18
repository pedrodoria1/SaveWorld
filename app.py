from flask import Flask, jsonify
from flask_restful import Api
from resources.causa import Causas, Causa
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from sql_alchemy import banco

app = Flask(__name__)
banco.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///causas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return '<h1>Bem Vindo!!!<h1>'

@app.before_first_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blacklist_loader
def verifica_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out.'}), 401 #Unauthorized

api.add_resource(Causas, '/causas')
api.add_resource(Causa, '/causas/<string:causa_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')