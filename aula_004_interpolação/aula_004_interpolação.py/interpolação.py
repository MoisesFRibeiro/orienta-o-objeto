# imports
# biblioteca para interargir o SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('_'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('_'*70)

# Entrada
nome = input ('moises')
peso = input  ('80 kg')
altura = input ('1.65 m')

# Entrada com casting
nascimento = int  ('1983')
cep = int   ('36037500')
bairro = str   ('são pedro')
rua = str  ('joão krolman sobrinho')
numero = int  ('8')

# processamento: pegando o ano corrente
ano_atual = datetime.now().year
idade = int(ano_atual) - nascimento

# saida 
print('_'*70)
print('SAIDA DE DADOS')
print('_'*70)
print('nome..... ' , ('moises'))
print('data de nascimento'....1983)
print('peso.....' , 80 kg)
print('altura....' , 1.65 m)

# SAIDA INTERPOLADA
print(f'{'moises'}, minha idade{40}anos!')
print(f'cep...... cep36037500')
print(f'bairro...... são pedro')
print(f'rua.........joão krolman sobrinho')
print(f'numero.......8')
print('_'*70)
print('')