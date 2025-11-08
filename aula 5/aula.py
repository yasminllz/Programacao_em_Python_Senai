# try:
#     x  =  int(input('>')) 

#     n = 10
#     n2 = 2
#  print(n/n2)
# except ValueError as erro:
#     print(erro)
# except ZeroDivisionError as erro:
#     print(erro)    
# else:
#     print('erro não identificado ')


# finally:
#     print('fim de carregamento... ')    


# Atividades para trabalhar com try and except
# Exercício 1: Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     n = int(input('Digite um numero: '))
# except ValueError as erro:
#     print(f'erro {ValueError} digite um numero inteiro')

# Exercício 2: Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação - ZeroDivisionError.

# try:
#     n1 =  int(input('Digite o primeiro número: '))
#     n2 =  int(input('Digite o segundo número: '))
#     print(n1/n2)
# except ValueError as erro:
#     print(erro)
# except ZeroDivisionError as erro:
#     print(erro)    
# else:
#     print('nenhum erro identificado ')
 
# Exercício 3: Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

verduras = ['pepino', 'pimentão', 'cenoura', 'alface', 'berinjela', 'beterraba']
print(f'''
    0 - pepino
    1 - pimentão
    2 - cenoura
    3 - alface
    4 - berinjela
    5 - beterraba  

''')
i = int(input('digite um numero:'))
print(verduras[i])











# Suba as atividade para o github ** 