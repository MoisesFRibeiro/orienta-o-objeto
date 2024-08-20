import os 


os.system('cls')

# definindo uma função 
def calcular_velocidade_media(km, horas, minutos, metros):
    # vm = deltaS/deltaT
    velocidade_media = km/horas/minutos/metros
    return velocidade_media

minutos = float(input('voce deseja informar em minutos ou horas: {minutos} ou {tempo}'))
metros = float(input('voce deseja informar em {km} ou {metros}'))

# calcular a velocidade media usando a função criada
Velocidade = calcular_velocidade_media(minutos, metros)

# exibir  o resultado 
print(f'a velocidade media é {Velocidade:.2f} km/h.')