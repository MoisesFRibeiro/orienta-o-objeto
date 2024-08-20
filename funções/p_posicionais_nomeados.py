import os


os.system('cls')

# definindo a função
def dados_paciente(nome= 'coly', nascimento=2005, peso= 46, altura= 1.68):
    print(f'Bem vindo(a) ao sistema senac, {nome}!')
    print(f'o ano de nascimento da  {nome} é {nascimento}.')
    print(f' o peso da {nome} é {peso}kg.')
    print(f'a altura da {nome} é {altura}m.')
    print('-'*70)

# inicio para lembrar
def posicional_nomeado(nascimento, nome ='coly',): # ok não funciona!!!
    print(f'Bem vindo (a) ao sistme senac, {nome}!')
    print(f'o ano de nascimento da {nome} é {nascimento}.')
    print('-'*70)

'''def nomeado_posicional(nome='coly', nascimento): # not ok! não funciona!!! 
    print(f'bem vindo (a) ao sistema senac, {nome}!')
    print(f'o ano de nascimento da {nome} é {nascimento}.')
    print('-'*70) 
'''
    # chamando as funções
dados_paciente()

dados_paciente(nome='isis', nascimento=1985, peso=46, altura=1.56)
dados_paciente(nascimento=2008, nome='Ágata', peso=46, altura=1.58)
dados_paciente(altura=1.66, peso=46, nome="Bia", nascimento=2008)  