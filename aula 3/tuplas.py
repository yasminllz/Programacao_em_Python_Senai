#lista
# numeros = [1,2,3]
#tuplas
# tupla = (102,5,6)
# tupla2 = tuple(range(1,11))
# tupla3 = 1,2,3,4,5,6,
#dicionario
# 'a':10
# 'b':20
# 'c':30

#e_comerce dicionario
print('------------------BEM-VINDO AO E-COMMERCE------------------------')
e_commerce = {
    'tenis nike':600.0,
    'camiseta adidas': 150.0,
    'fone': 250.50,

}

carrinho = []
valores = []

produto_1 = input('digite o nome do produto: ')
produto_2 = input('digite o nome do produto: ')

carrinho.append (produto_1)
carrinho.append (produto_2)
print(carrinho)

valores.append(e_commerce[produto_1])
valores.append(e_commerce[produto_2])

print('R$', valores)
somar = sum(valores)
print('R$', somar)