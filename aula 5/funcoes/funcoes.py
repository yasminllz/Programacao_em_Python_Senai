peso = 65.00 # global 


# 1º cria a função 
def imc():
    ''' Calcula o IMC '''
    
    peso = 55 # float(input('Peso:')) # locais
    altura  =   float(input('Altura:')) # locais
    imc  =  peso / (altura ** 2)
    print(imc)


print(peso)
print(peso)




imc() # 2º chama para funcionar 







# # 1

# def comparar():
#     n1 = int(input('nº: '))
#     n2 = int(input('nº: '))

#     if n1 % 2 == 0 and n2 % 2 == 0:
#         print('Ambos são pares')
#     elif  n2 % 2 == 1 and n2 % 2 == 1:
#         print('Nenhum é par')
#     else: 
#         print('Apenas 1 é par')    

# comparar()            

# # # 2

# # def multiplicar(x,y,z):
# #     return x * z * y

# # # print(multiplicar(20,2,3)) 


# # # # 3

# # def elevado():
# #     n =  int(input('numero = '))
# #     elevado   =  n ** 2
# #     print(elevado)

# # elevado()    



# # #  4

# # def display(idade):
# #     if idade == 18:
# #         print('Você tem 18 anos')
# #     else:
# #         print('Você não tem 18 anos... ')

# # display(25)            ]




# #  5 

# def descobrir(ano, ano_nasc, mes):
    
#     if mes < 11:
#         cal =  (ano  - ano_nasc   ) 
#         print(cal)
#     else:
#         cal =  ano   -  1 -  (ano_nasc)
#         print(cal)
# descobrir(2025,2000,10)            


# #  6

def br(ano , lista):
    if ano in lista:
        print('O Brasil ganhou neste ano')

    else:
        print('Brasil não ganhou')


anos = [1958, 1962, 1970, 1994 , 2002.]

br(1999,anos)            


# 7

def restaurante():
    produtos = ['macarronada', 'salada', 'sorvete', 'sanduiche']
    deseja_pedir = input('Deseja oedir')
     
    carrinho  = [] 

    while deseja_pedir == 'sim':
          produto =  int(input(f'produtos -> {produtos}'))
          carrinho.append(produtos[produto]) 
          print(carrinho)
        
          deseja_pedir = input('Deseja continuar? ')

    else:
        print('Obrigada volyte sempre!')              
restaurante()        