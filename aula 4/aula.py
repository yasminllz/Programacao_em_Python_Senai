# # sinais ariméticos 
# # +    -    *   /   //    %    **0.5
# # Saida é sempre um número

# n1  = 10
# n2  = 20

# print(n1  +  n2 )
# print(n1  -  n2 )
# print(n1  *  n2 )
# print(n1  /  n2 )

# # primeiro valor decimal  
# print(n1  //  n2 )

# # resto da conta de divisão 
# print(10  %   2 )

# # sinais lógicos -  saída é sempre True ou False
# n1  = 10
# n2  = 2
# print(n1 > n2)# maior
# print(n1 < n2)# menor  
# print(n1 >= n2)# maior ou igual
# print(n1 <= n2)# menor ou igual
# print(n1 != n2)# diferente
# print(n1 == n2)# igual


# print('objeto', 10, n1) # output -- saída

# nome = input('digite seu nome: ') # input -- entrada

# # o Input naturalmente gera um texto 

# n1  =  float(input('Digite um número: '))
# n2  =  float(input('Digite outro número: '))
# print(n1 + n2)

# n1  =  float(input('Digite um número: '))
# n2  =  float(input('Digite outro número: '))
# print(n1 - n2)

# n1  =  float(input('Digite um número: '))
# n2  =  float(input('Digite outro número: '))
# print(n1 / n2)

# n1  =  float(input('Digite um número: '))
# n2  =  float(input('Digite outro número: '))
# print(n1 * n2)

# concatenar outras formas
# print('Nome', nome, 'idade: ',idade)
# print(f'Nome {nome} idade {idade}')
#concatenação
# nome = input('digite seu nome: ')
# idade = int(input('digite sua idade:'))
# endereco = input('digite seu endereço:')
# curso = input('curso:')
# salario = float(input('digite seu salario:'))
#contatenar com virgula
# print('nome: ', nome)
# print('sua idade é : ', idade)
# print('seu endereço é : ', endereco)
# print('seu curso é : ', curso)
# print('salario : ', salario)

#pular linha
# \n
# f'''
# f''' jeijfgnjfng {}'''

# ----------------------------------------- ATIVIDADES ------------------------------------------------------------------------------
# 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
# 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
# 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
# 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
# 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.


# 1
print("  RESULTADO DO NÚMERO AO QUADRADO  ")
num = int(input("digite um numero: "))
quadrado = num**2
print(f"o numero é: {num} \n ele ao quadrado é: {quadrado}")

# 2 
print("  NOME COMPLETO  ")
nome = input("Digite o seu nome: ")
sobrenome = input("digite o seu sobrenome:")
print(f"Seu nome completo é: {nome} {sobrenome}")

#3 
print("  NÚMEROS COM STRINGS ")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
print(str(num1),str(num2))

#4
print("  NÚMERO INTEIRO AO FINAL DA PALAVRA  ")
palavra = "Python"
inteiro = int(input("Digite um número inteiro:"))
print(f"{palavra}{inteiro}")

#5
print("  DIGITE O FINAL DA FRASE ")
frase = "O curso em Python tem atividades práticas "
palavra_1 = input("digite uma palavra:")
print(f"{frase} {palavra_1}")





