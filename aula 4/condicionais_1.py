# Desafio 1: - Condicionais

# Sistema de Reservas de Hotel:

# Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias.

# - Cadastro de Cliente:

# O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.

# - Reservas de Quartos:

# O sistema deve oferecer 3 tipos de quartos:

# "Simples", "Duplo" e "Luxo".

#    Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.
 
#  - Cálculo da Estadia:

# O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.

print(' ---------------------- CADASTRO DE CLIENTE -------------------------')
 atividade 2 hospedagem: 

quartos  =  ['','simples','duplo','luxo']
valores =  [0,100,150,250]

pessoas = int(input('Quantas pessoas vão se hospedar: '))

if pessoas == 1:
    nome =  input('NOme: ')
    idade = int(input('Idade: '))

    print('Olá', nome)

    escolha  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade = int(input('Dias: '))
    calculo =  valores[escolha]  *  quantidade

    print('R$', calculo)
    print('Dias', quantidade)

    formas_pag = ['', 'PIX','CC','CD']
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')



if pessoas == 2:
    nome1 =  input('Nome: ')
    idade1 = int(input('Idade: '))

    nome2 =  input('Nome: ')
    idade2 = int(input('Idade: '))


    print('Olá', nome1)

    escolha1  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade1 = int(input('Dias: '))
    calculo1 =  valores[escolha1]  *  quantidade1

    print('R$', calculo1)
    print('Dias', quantidade1)


    formas_pag = ['', 'PIX','CC','CD']
    print(formas_pag)    
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')


    print('--------------------------------')

    print('Olá', nome2)

    escolha2  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade2 = int(input('Dias: '))
    calculo2 =  valores[escolha2]  *  quantidade2

    print('R$', calculo1)
    print('Dias', quantidade1)


    
    formas_pag = ['', 'PIX','CC','CD']
    print(formas_pag)
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')

    print('----------------------------------')


elif pessoas == 3:
    nome1 =  input('Nome: ')
    idade1 = int(input('Idade: '))

    nome2 =  input('Nome: ')
    idade2 = int(input('Idade: '))

    nome3 =  input('Nome: ')
    idade3 = int(input('Idade: '))


    print('Olá', nome1)

    escolha1  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade1 = int(input('Dias: '))
    calculo1 =  valores[escolha1]  *  quantidade1

    print('R$', calculo1)
    print('Dias', quantidade1)

    
    formas_pag = ['', 'PIX','CC','CD']
    print(formas_pag)
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')

    print('--------------------------------')

    print('Olá', nome2)

    escolha2  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade2 = int(input('Dias: '))
    calculo2 =  valores[escolha2]  *  quantidade2

    print('R$', calculo1)
    print('Dias', quantidade1)


    formas_pag = ['', 'PIX','CC','CD']
    print(formas_pag)
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')


    print('--------------------------------')

    print('Olá', nome3)

    escolha3  =  int(input(f'''
    escolha p seu quarto

    1 - {quartos[1]} R$ {valores[1]} 
    2 - {quartos[2]} R$ {valores[2]} 
    3 - {quartos[3]} R$ {valores[3]} 
    
    '''))
    
    quantidade3 = int(input('Dias: '))
    calculo3 =  valores[escolha3]  *  quantidade3

    print('R$', calculo3)
    print('Dias', quantidade3)

    
    formas_pag = ['', 'PIX','CC','CD']
    print(formas_pag)
    pag =  int(input('Forma de pagamento: '))
    print('forma de pagamento - ', formas_pag[pag])
    print('Obrigada volte sempre')

    print('----------------------------------')



