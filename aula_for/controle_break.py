import os


os.system('cls')

print('_'*70)
print('estrutura de controle: break')
print('='*70)

print()

for c in range(0, 10):
    print(f'valor: {c}')

    # condição para terminar a contagem
    if(c == 5):
       print(f'a contagem interrompida no: {c}')
       break
print('_'*70)
print('fim do programa!')
print()      