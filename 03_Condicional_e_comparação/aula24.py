# Operadores in e not in
# String são iteráveis
#  0 1 2 3 4 5
#  o t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('vio' in nome)
# print('vio' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o nome que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está {nome}')
else:
    print(f'{encontrar} não está em {nome}')