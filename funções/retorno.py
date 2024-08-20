import os


os.system('cls')

# definindo uma função
def calcular_velocidade_media(distancia, tempo):
    # Vm = deltaS/ deltaT
    velocidade_media = distancia / tempo
    return velocidade_media
distancia = float(input('digite a distancia percorrida (em km ): '))
tempo = float (input('digite o tempo gasto (em horas): '))

# calcular a velocidade media usando a função criada 
velocidade = calcular_velocidade_media(distancia, tempo)

# exibir o resultado
print(f'a velocidade média é {velocidade:.2f} km /h.')