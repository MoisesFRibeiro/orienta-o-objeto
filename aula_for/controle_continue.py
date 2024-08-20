import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE: CONITNUE')
print('='*70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 esta fora do loop, se retirar a linha abaixo,
        # ele não aparecera na saida, deixe para verificação 
        print(f'o numero {c} esta fora do loop')
        continue # salta eo ciclo continua
    print(f'o numero é {c}')

print('-'*70)
print()