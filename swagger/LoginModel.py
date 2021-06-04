from flask_restx import fields

from controllers.LoginController import api

login_fields = api.model('LoginDTO', {
    'login': fields.String,
    'senha': fields.String
})

user_fields = api.model('UsuarioDTO', {
    'name': fields.String,
    'email': fields.String,
    'token': fields.String
})
