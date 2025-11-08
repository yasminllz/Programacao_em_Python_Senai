
# import random


# numero =  random.randint(1,6)
# match numero:
#     case 1:
#         print('😁')
#     case 2:
#         print('😈')
#     case 3:
#         print('🤡')
#     case 4:
#         print('😎')   
#     case 5:
#         print('🎃')   
#     case 6:
#         print('🤑') 


# 2 verifique se e positivo, negativo ou zero

# n  =  int(input('Digite um numero: '))


# match n:
#     case 0:
#         print('Zero')
#     case n if n > 0:
#         print('positivo')
#     case n if n < 0:
#         print('Negativo')
#     case _:
#         print('Desconhecido')            



#1 verifique se o numero e par ou impar 
#         numero = int(input('numero: '))

# match numero:
#     case numero if numero % 2 == 0:
#         print('Par')
#     case _:
#         print('Impar')


 #3 verifique se um string é vazia ou nao

# dado = input('digite: ')
# match dado:
#         case dado if dado == '':
#             print('está vazia')
#         case _:
#             print('não está vazia')
 
 #4 verifique se o numero e maior , menor ou igual a 10

# numeros = int(input('numero:'))




# 5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)***

# idade = int(input('Idade: '))



# match idade:
#     case idade if idade >= 65:
#         print('idoso')
#     case idade if idade >= 35 and idade <=64:
#         print('Adulto')   
#     case idade if idade >= 18 and idade <=34:
#         print('jovem')  
#     case idade if idade >= 14 and idade <=17:
#         print('Adolescente')                   
#     case _:
#         print('Criança')   


#TABUADA

# mul = int(input('Multiplicador: '))
# for numero in range(11):
#     calculo =  numero * mul
#     print(mul, 'X', numero, '=', calculo)


# carrinho = []
# for n in range(10):
#     produto = input('produto: ')
#     carrinho.append(produto)
#     print(carrinho)


# for    while


# while True:
#     print('inifinito')




# contador =  0


# while contador <= 3:
#     print(contador)
#     contador = contador + 1



# if else elif 
# match case
# for while




ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },


        'roupas':{
            'camiseta':150.0,
            'calça':250.0


        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }



}




carrinho = []
valores  =  [] # criar a lista valores


deseja = input('deseja comprar - sim / não ?')
while deseja == 'sim':
    secao = input('Secao - celulares roupas ou acesorios')
    p1 = input(f'Produto: {ecommerce[secao]}')
    carrinho.append(p1) # adicionamos o produto
    valores.append(ecommerce[secao][p1])
    print(carrinho)
    total = sum(valores)
    print('R$', total)
    deseja = input('Deseja continuar   - sim / não?')
else:
    print('Obrigada volte sempre!')   