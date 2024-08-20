# Trabalho de estrutura de dados SET
# Senac Minas Gerais/ Juiz de Fora
# Aluno: Moises De Souza Ribeiro
# Turma: 0152
# Ano: 2024
# Excluindo material escolar de uma lista 
     
import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: SET')
print('='*70)

# declarando lista de materiais
materiais_escolar = ["caneta", "lapis", "papel", "borracha"]
materiais_escolar_2 = ["livros", "pincel", "tinta", "caderno"]
excluir = []

while True:

# escolhendo qual material deseja excluir
    excluir = input('selecione qual material deseja excluir: ')

    if excluir.lower():
     materiais_escolar.remove('')

    elif (excluir != materiais_escolar):
       print('continue digitando......')

# escolhendo qual material deseja excluir na lista 2
    elif excluir.lower():
        materiais_escolar_2.remove('')

    else:
              
        print(f'a lista de materiais final foi:{materiais_escolar} ')

