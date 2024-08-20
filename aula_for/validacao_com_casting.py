import os


os.system('cls')

print('_'*50)
print('estrutura de controle e validacão com casting')
print('='*50)

soma = 0

for c in range(0, 5):
    numero = input('digite um numero[0, 5]: ')

    # validacão
    if(not(numero.isnumeric())):
        print(f'"{numero}"entrada invalida!')
        print()
    else:
        # casting da variavel, ou seja, vai virar um numero inteiro
        numero = int(numero)

        # validando o intervalo pedido
        if (numero>= 0 and numero <=5):
            print(f'o numero {numero} esta dentro do intervalo[0,5!]')
            print()
        else:
            print(f'"{numero}"entrada invalida!')
            print()


print('_'*70)
print()            