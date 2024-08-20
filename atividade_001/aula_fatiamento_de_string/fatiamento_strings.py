import os


os.system('cls')

print('_'*70)
print('fatiamento de strings')
print('='*70)

frase = 'strings em python!'

# exibindo a string original
print(f"string original: {frase}")

# fatiamento: acessando párte especifica da string
# primeiros cincos caracteres
primeiros_cincos = frase[:5]
print(f'primeiros cincos caracteres: {primeiros_cincos}')

# ultimos dez caracteres
ultimos_dez = frase[-10:]
print(f"ultimos dez caracteres: {ultimos_dez}")
