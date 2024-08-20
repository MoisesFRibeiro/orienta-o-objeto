# zero division error
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("erro: divisão por zero!")

# value error
try:
    numero = int("não é um numero")
except ValueError:
    print("erro: valor invalido!") 

# type error
try:
    soma = '5' + 5 
except TypeError:
    print("erro: tipo incompativel!")

# indexerror
lista = [1, 2, 3]
try:
    item = lista[5]
except IndexError:
    print("erro: indice fora do intervalo da lista!")

# keyerror
dicionario = {'chave', 'valor'}
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print("erro: chave não encontrada no dicionário!")

# file no found error
try:
    with open('arquivo_inexitente.txt' ,'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('arquivo não encontrado!')

# IOerror
try:
    with open('arquivo.txt','w') as arquivo:
        conteudo = arquivo.read()
except IOError:
    print("erro: operação de E/S falhou!")

# Attributerror
class exemplo:
    def __init__(self):
        self.atributo = "valor"

objeto = exemplo()
try:
    print(objeto.atributo_inexistente)
except AttributeError:
    print("erro: atributo não encontrado no objeto!")

# importerror
try:
    import modulo_inexistente # type: ignore ignora o erro
except ImportError:
    print('erro: modulo não encontrado!')

# run time error
try:
    raise RuntimeError("este é um erro de execução!")
except RuntimeError as e:
    print('erro: {e}')                             