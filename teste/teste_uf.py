import os 


os.system('cls')

UF = []
while (True):
    UF = str(input('Digite aqui sua UF:............'))
    if UF.isnumeric():
        print(f'"{UF}" entrada invalida!')
        
