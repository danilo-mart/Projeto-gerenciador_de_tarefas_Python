import random
import string

API_HOST = '127.0.0.1'
API_PORT = 5000
API_BASE_URL = '/api'

# Gera uma chave aleatória para geração do JWT
gen = string.ascii_letters + string.digits + string.ascii_uppercase
SECRET_KEY = ''.join(random.choice(gen) for i in range(32))


#Configuração MySQL
MYSQL_HOST = 'mysqlgerenciadordetarefas.cjayfxhtohhe.us-east-2.rds.amazonaws.com'
MYSQL_PORT = 3306
MYSQL_USER = 'danilo'
MYSQL_PASSWORD = '101924Sql'
MYSQL_DATABASE = 'gerenciador_tarefas'

DEBUG = True