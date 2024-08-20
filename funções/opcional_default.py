import os


# definição da função
def multiplicar(a, b=1):
    return a * b

os.system('cls')

resultado1 = multiplicar(5)
resultado2 = multiplicar(5, 2)

print(f'o primeiro resultado: {resultado1}')
print(f'o segundo resultado: {resultado2}')
print()