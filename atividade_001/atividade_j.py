#Faça um programa com entrada de dados para calcular o perímetro de um retângulo.
# imports
import os


# Limpando a Biblioteca
os.system('cls')

# Entrada
altura = float(input('entre com a medida da altura'))
largura = float(input('entre com a medida da largura'))

# Processamento
perimetro = 2 * (altura + largura)

# Saida
print(f'o retangulo de medidas {altura} e {largura} tem o perimetro de {perimetro}')