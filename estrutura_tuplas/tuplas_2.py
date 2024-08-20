import os 


os.system('cls')

# solicitar ao usuario a quantidade de eleementos na tupla
numero_elementos = int(input("quantos elementos na tupla? "))

# inicializar uma lista vazia  para armazenar os elementos
elementos = [ ]

# estrutura de repetição para obter os elementos  do usuario
for i in range(numero_elementos):
    while True:
        valor = input (f"digite o valor {i + 1 }: ")
        if valor.isdigit(): # verifica sea entrada é um numero
            elementos.append(int(valor))
            break
        else:
            print('entrad invalida. digite um numero: ')

# coverte a lista para uma tupla
tupla = tuple(elementos) 

print('_'*70)
# exebir a tupla criada
print(f"tupla criada: {tupla}")
print('_'*70)

# estrutura de repetição para permitir tuplas mutiplas
# operações até que o usuario deseje sair
while True:
    # condicional para verificar a presença de 
    # um numero especifico 
    valor = int(input(" verificar se o numero é tupla: "))

    if valor in tupla:
        print(f"o numero {valor} esta na tupla.")
        # contar quantas vezes o n umero aparece 
        contagem = tupla.count(valor)
        print(f"o numero {valor} aparece {contagem} vez(es).")

        indice = tupla.index(valor)
        print(f"a 1º ocorrencia de {valor} esta no indice {indice}.")
    else:
        print(f"o numero {valor} não esta na tupla.")

# perguntar ao usuario se ele deseja realizar 
# outra correção ou sair 
    continuar = input("deseja continuar ? (s/n):").lower()
    if continuar != "s":
        print(f'encerrando o programa. Até mais!')
        break
print('_'*70)
print('fim do programa!')
print()     