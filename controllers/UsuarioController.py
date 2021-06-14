import json

from flask import Blueprint, Response, request
from flask_restx import Namespace, Resource, fields

import config
from dtos.ErroDTO import ErroDTO
from dtos.UsuarioDTO import UsuarioBaseDTO, UsuarioCreateDTO
from services.UsuarioService import UsuarioService
from utils import Decorators
from utils.Criptografia import criptografar_senha

usuario_controller = Blueprint('usuario_controller', __name__)

api = Namespace('Usuário')

user_fields = api.model('UsuarioBaseDTO',{
    'nome': fields.String,
    'email': fields.String,

})

@api.route('', methods=['POST'])
class UsuarioController(Resource):
    def post(selfs):
        try:
            body = request.get_json()

            erros = []

            if not body:
                return Response(
                    json.dumps(ErroDTO(400, "Body da requisição está vazio").__dict__),
                    status=400,
                    mimetype='application/json'
                )

            if not "nome" in body:
                erros.append("Campo 'nome' é obrigatório.")

            if not "email" in body:
                erros.append("Campo 'email' obrigatório")

            if not "senha" in body:
                erros.append("Campo 'senha' obrigatório")

            if erros:
                return Response(
                                json.dumps(ErroDTO(400, erros).__dict__),
                                status=400,
                                mimetype='application/json'
                                )

            usuario_criado = UsuarioService().criar_usuario(body['nome'], body['email'], body['senha'])

            if not usuario_criado:
                return Response(
                    json.dumps(ErroDTO(400, "E-mail já cadastrado no sistema").__dict__),
                    status=400,
                    mimetype='application/jason'
                )

            return Response(
                json.dumps(UsuarioCreateDTO(usuario_criado.id, usuario_criado.nome, usuario_criado.email, usuario_criado.senha).__dict__),
                status=201,
                mimetype="application/json"
            )
        except Exception:
            return Response(
                json.dumps(ErroDTO(500, 'Não foi possível sua requisição, favor tentar novamente').__dict__),
                status=500,
                mimetype="application/jason"
            )