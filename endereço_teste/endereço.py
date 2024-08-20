import re

# criando dicionário e dados a serem inseridos
rua = []
numero = []
cep = []
bairro = []
cidade = []
estado = []
endereço = {}

# recebendo entrada de dados
rua = input('digite o nome da rua: ')
numero = input('digite o numero: ')
cep = input('digite o numero do cep: ')
bairro = input('digite o nome do bairro: ')
cidade = input('digite o nome da cidade: ')
estado = input('digite o estado: ')

def cadastro(endereço):
    """metodo para validar argumentos

    Args:
        rua = (nome da rua)
        numero = (numero da rua)
        cep = (cep da rua)
        bairro = (nome do bairro)
        cidade = (nome da cidade)
        estado = (nome do estado)
    """    
    endereço =  