from flask_restful import Resource, reqparse
from models.causa import CausaModel
from flask_jwt_extended import jwt_required

class Causas(Resource):
    def get(self):
        return {'causas': [causa.json() for causa in CausaModel.query.all()]}

class Causa(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('autor')
    atributos.add_argument('meta')
    atributos.add_argument('descricao')

    def get(self, causa_id):
        causa = CausaModel.find_causa(causa_id)
        if causa:
            return causa.json()
        return {'message': 'Cause Not Found.'}, 404

    @jwt_required
    def post(self, causa_id):
        if CausaModel.find_causa(causa_id):
            return{"message": "Causa id '{}' já existe.".format(causa_id)}, 400 #Bad Request
        dados = Causa.atributos.parse_args()
        causa = CausaModel(causa_id, **dados)
        try:
            causa.save_causa()
        except:
            return {"message": "An error ocurred trying to create a cause."}, 500 #Internal Server Error
        return causa.json(), 201

    @jwt_required
    def put(self, causa_id):
        dados = Causa.atributos.parse_args()
        causa_encontrado = CausaModel.find_causa(causa_id)
        if causa_encontrado:
            causa_encontrado.update_causa(**dados)
            causa_encontrado.save_causa()
            return causa_encontrado.json(), 200
        causa = CausaModel(causa_id, **dados)
        causa.save_causa()
        return causa.json(), 201 #Created

    @jwt_required
    def delete(self, causa_id):
        causa = CausaModel.find_causa(causa_id)
        if causa:
            causa.delete_causa()
            return {'message': 'Cause Deleted'}
        return {'message': 'Cause Not Found.'}, 404