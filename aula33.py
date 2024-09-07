'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
'''
numero_str = input("Digite um número inteiro: ")

try:
    numero_int = int(numero_str)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O número {numero_int} é {par_impar_texto}')
except:
    print('Isso não é um número inteiro')

'''
Faça um programa que pergunta a hora ao usuário e, baseando-se
no horário descrito, exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
'''
entrada = input(f"\nDigite a horam em números inteiros: ")

try:
    hora = int(entrada)

    if hora <= 11:
        print('Bom dia!!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!!')
    else:
        print('Essa hora não existe')
except:
    print('Por favor digite apenas numeros inteiros')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''
nome = input(f'\nDigite seu nome: ')

CURTO = len(nome) <= 4
MEDIO = len(nome) >= 5 and len(nome) <= 6


if CURTO:
    print('Seu nome é curto')
elif MEDIO:
    print('Seu nome é médio')
else:
    print('Seu nome é muito grande')