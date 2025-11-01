
# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

# num = int(input('Digite um numero:'))
# if num == 0:
#     print('numero digitado igual a zero')
# elif num > 0:
#     print('Numero Positivo')
# else:
#     print('Numero Negativo')


# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

# idade = int(input('Digite a sua idade:'))
# if idade > 60 or idade >= 16 and idade <= 17:
#     print('Opcional Votar')
# elif idade >=18 and idade <=60:
#     print('Obrigatorio votar')
# else:
#     print('Voce não Pode Votar')

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.


# aleatorio = 9
# qualquer = aleatorio % 2
# if qualquer == 0 :
#     print('Numero Par')
# else:
#     print('Numero Impár')


# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
print('Digite tres numeros para criar um triângulo')
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
num3 = int(input('Digite o terceiro numero:'))

if num1 == num2 == num3:
    print('Triângulo equilátero ')
elif num1 == num2 or num1 == num3 or num2 == num3:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')


# 5*

# Determine se um número é múltiplo de 5 e 7.

number = int(input('numero:'))
multiplo_5 = number %5
multiplo_7 = number %7
if multiplo_5 == 0 and multiplo_7 == 0:
    print(f'O numero {number} e multiplo de 5 e 7')
elif multiplo_5 == 0:
    print('multiplo de 5')
elif multiplo_7 == 0:
    print('muultiplo de 7')
else:
    print('o numero não e multiplo de 5 e 7 ')

# 6*

# Verifique se um número é positivo e maior que 10

n = int(input('numero:'))
if n > 10:
    print(f'Numero positivo, {n} é maior que 10')
elif n < 0:
    print('O Numero e negativo')
else:
    print('numero positivo mas menor que 10')
# 7*

# Verifique se um número é divisível por 3 ou 5.

nu = int(input('numero:'))
divi_3 = nu % 3
divi_5 = nu % 5
if divi_3 == 0 and divi_5 == 0:
      print(f'O numero {nu} e divisívrel por 3 e 5')
elif divi_3 == 0:
    print('Divisível por 3')
elif divi_5 == 0:
    print('Divisívell por 5 ')
else:
    print('o número não e divisível por 3 e nem por 5 ')