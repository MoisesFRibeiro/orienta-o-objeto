import os


os.system('cls')

print('_'*70)
print('estrtura while else continue')
print('='*70)

print()

contador = 0 # flag

while (contador <=10):

    # soma p contador
    contador += 1 # é o mesmo que o contador = contador + 1 

    if (contador % 2 == 0): # pulando os pares
        continue
    print(f'contador = {contador}')

else:
    print(f' o bloco do while...else: contador em {contador}!')

print('_'*70)
print('fim do programa!')
print()