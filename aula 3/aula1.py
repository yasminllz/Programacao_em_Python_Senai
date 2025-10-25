 #e_comerce
#lista
carrinho = []
meu_total = []

lista_produtos = ['','hd','ssd', 'iphone17', 'pc dell']
valores_produtos = [0,500.55, 20.5, 7000.0,800.99]
print(f'''
1 - {lista_produtos[1]} = R${valores_produtos[1]}
2 - {lista_produtos[2]} = R${valores_produtos[2]}
3 - {lista_produtos[3]} = R${valores_produtos[3]}
4 - {lista_produtos[4]} = R${valores_produtos[4]}
''')

#variaveis que vão escolher o produto da lista 
produto_1 = int(input('id do produto: '))
produto_2 = int(input('id do produto: '))
produto_3 = int(input('id do produto: '))


carrinho.append(lista_produtos[produto_1])
print('Voce inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_1])
print(' R$ ', sum(meu_total))

carrinho.append(lista_produtos[produto_2])
print('Voce inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_2])
print(' R$ ', sum(meu_total))

carrinho.append(lista_produtos[produto_3])
print('Voce inseriu no seu carrinho - ', carrinho)
meu_total.append(valores_produtos[produto_3])
print(' R$ ', sum(meu_total))

print('----------------------------------------------------------')
print('Seu Pedido ficou R$', sum(meu_total))
print(carrinho)
print('----------------------------------------------------------')

print('''
1 - Pix
2 - Cartão de Credito (CC)
3 - Cartão de Debito  (CD)
''')
forma_pag = [' ', '1 - PIX', '2 - CC', '3 - CD']
pag = int(input('ESCOLHA A FORMA DE PAGAMENTO A PARTIR DO ID: '))
print('Sua forma de pagamento é', forma_pag[pag], 'Obrigada volte sempre!')
























