# Exercícios com funções:
# variáveis locais, globais e parâmetros

# 1
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def comparação():
    print( '---------------COMPARAÇÃO DE 2 NUMEROS(PAR OU IMPAR)------------------')
    n1 = int(input('digite um numero:'))
    n2 = int(input('digite um numero:'))
    veri = n1 % 2 == 0
    ver = n2 % 2 == 0
    print('é par?', veri)
    print('é par?',ver)

# comparação()

# 2
# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar():
    print('-----------------MULTIPLICAÇÃO DOS TRES NUMEROS---------------------')
    num1 = int(input('digite um número:'))
    num2 = int(input('digite um número:'))
    num3 = int(input('digite um número:'))
    mul = num1 * num2 * num3 

    print(f'o resultado da multiplicação é {mul}')

# multiplicar()

# 3
# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado():
    print('---------------VALOR ELEVADO DE UM NUMERO----------------------------')
    elev = int(input("digite um numero para descobrir ele ao quadrado: "))
    quadrado = elev**2
    print(f"o numero é: {elev} \n ele ao quadrado é: {quadrado}")

# elevado()

# 4
# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.

def mensagem ():
    print('------------------DIGITE 18, PARA RECEBER UMA IMAGEM PERSONALIZADA------------------------ ')
    men = int(input('Digite o numero chave:'))
    if men < 18:
        print('digite o numero corretamente')
    elif men > 18:
        print('digite o numero corretamente')
    else:
        print('Voçê acabou de receber a mensagem personalizada🥳,  Que voçê tenha um otimo final de semana 🙌😁')
    
# mensagem ()

# 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.


def descobrir(ano, ano_nascimento, mes):
    print('-----------------------------DESCOBRIR A IDADE DE PESSOA----------------------------------')
    if mes <11:
        cal = (ano - ano_nascimento)
        print(cal)
    else:
        cal = (ano -ano_nascimento - 1)
        print(cal)
# descobrir(2025,2007,12)

# 6
# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.


def br(ano , lista):
    print('------- DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999---------- ')
    if ano in lista:
        print('O Brasil ganhou neste ano')

    else:
        print('Brasil não ganhou')


anos = [1958, 1962, 1970, 1994 , 2002.]

# br(1999,anos)            
   

# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
# 1 - Função - cumprimentar o cliente
# 2 - Função - restaurante
# 3 - Sugestão utilize listas e loops
print('--------------------------- SISTEMA DE RESTAURANTE------------------------')
def restaurante():
    produtos = ['macarronada', 'salada', 'sorvete', 'sanduiche']
    deseja_pedir = input('Deseja pedir algo mais?')
     
    carrinho  = [] 

    while deseja_pedir == 'sim':
          produto =  int(input(f'produtos -> {produtos}:'))
          carrinho.append(produtos[produto]) 
          print(carrinho)
        
          deseja_pedir = input('Deseja continuar? ')

    else:
        print('Obrigada volte sempre!😁')              
restaurante()        

# Subir para o Github** 