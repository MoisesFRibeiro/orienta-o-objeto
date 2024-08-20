import os


os.system('cls')

print('_'*70)
print('estrutura de controle while else')
print('='*70)
print()

print()

contador = 1

while contador < 7:
    print("contador é:", contador)
    contador += 1

    # se eu tirar essa condicional o else será executado
    if contador == 4:
        print(f'contador chegou em {contador}. break no while!')
        break
else:
    print("while finalizado!")

print('-'*70)
print()