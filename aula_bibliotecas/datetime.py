# importando as bibliotecas
import os


# podemos importar somente as funções que queremos utilizar
import datetime


# limpando o terminal
os.system('cls')

# declarando uma variavel para data
data = datetime.now()

# declarando uma variavel data formatada
data_formatada = data.strftime('%d%m%Y') 

# declarando uma variavel data e hora formatada
data_hora_formatado = data.strftime('%d%m%Y %H:%M')

print(f'data formatada: {data_formatada}')
print(f'data e horas formatadas: {data_hora_formatado}')

# recebendo o ano 
data_atual = datetime.date.today( )
nascimento = 1970
idade = data_atual.year - nascimento

# imprimindo a data atual e nascimento
print('-'*70)
print(f'data atual no sistema: {data_atual} ')
print(f'nascimento........: {nascimento}')
# imprimindo só o ano
print(f'ano atual.........: {data_atual.year}')
# imprimindo so a idade
print(f'sua idade é ......: {idade}anos')
print('-'*70)
