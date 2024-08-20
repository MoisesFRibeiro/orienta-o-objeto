
#C) A empresa "SafeDrive" está desenvolvendo um sistema de monitoramento de velocidade para ajudar
# a promover a segurança nas estradas. Eles precisam de um programa que permita aos usuários inserir
# a velocidade de um carro e, em seguida, exibir na tela uma mensagem adequada com base na velocidade
# fornecida. O objetivo principal é alertar os motoristas caso ultrapassem o limite de velocidade de 60 km/h,
# incentivando-os a dirigir dentro dos limites legais e, assim, reduzir o risco de acidentes.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# aurtor: moises de souiza ribeiro
# data: 26/04/2024
# atividade de condicionais: c

# importando a Biblioteca
import os


# limpando a biblioteca
os.system('cls')

print('-'*70)
print('atividade de condicionais: C')
print('='*70)

# entrada
velocidade = float(input('digite aqui sua velocidade '))

# condicional
if velocidade > 60:
    
# saida 
   print(f' {velocidade} km/h esta acima do limite permitido')

else: 
    print(f' {velocidade} km/h esta dentro da velocidade permitida')    