


# 0 escreva um programa que use a função range() para gerar os pares de 2 a 20 e, eseguida imprima cada numero 

pares = list(range(2,21,2))
print(pares)

# 1 crie uma lista chamada numeros que contenha os numeros que contenha os numeros inteiros de 1 a 10 e imprima-os na tela 

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

# 2 acesse e imprima o terceiro elemento da lista 

print(numeros[2])

# 3 adiocione o numero 9 a lista numeros e imprima a lista atualizada

numeros.append(9)
print(numeros)

# 4 remova o numero 5 a lista de numeros e imprima a lista resultante

numeros.remove(5)
print(numeros)

# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista 
# `numeros` e imprima o resultado.


carros = ['Jeep','BMW','Ferrarri']


# numeros.extend([carros])


# numeros += (carros)
print(numeros, carros)