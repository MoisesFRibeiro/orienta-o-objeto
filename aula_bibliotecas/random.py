import random
import os


os.system('cls')

print('-'*70)
print('biblioteca random')
print('='*70)

print('numero aletório')
numero_aleatório = random.random()
print(f'o numero gerado foi: {numero_aleatório}')
print('-'*70)

print('numero aleatório inteiro')
aleatório_inteiro = random.randint(1,20)
print(f'o numero inteiro gerado foi: {aleatório_inteiro}')
print('_'*70)

print('numero aleatório decimal no intervalo')
aleatório_decimal = random.uniform(1,10)
print(f'o numero decimal gerado foi: {aleatório_decimal}')
print('-'*70)

print('sorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'lista: {lista}')
print(f'o nome escolhido foi: {nome_sorteado}')
print('-'*70)

print('embaralhar sequência')
lista2 = ['Ágata', 'Coly', 'Isis', 'Bia']
print(f'lista antiga: {lista2}')

# embaralhado = list(random.shuffle(lista)) dá erro
# embaralhado = random.shuffle(lista) saida vazia
random.shuffle(lista2)
print(f'lista nova; {lista2}')
print('-'*70)

print('retornos de elemento unico de uma população')
numeros = [1,2,3,4,5,6,7]
amostra_aleatória = random.sample(numeros, 5)
print(f'retorno da amostragem: {amostra_aleatória}')
print('-'*70)
