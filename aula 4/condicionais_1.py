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

# Cadastro de até 3 clientes
cliente1_nome = input("Digite o nome do 1º cliente: ")
cliente1_idade = int(input("Digite a idade do 1º cliente: "))

cliente2_nome = input("Digite o nome do 2º cliente: ")
cliente2_idade = int(input("Digite a idade do 2º cliente: "))

cliente3_nome = input("Digite o nome do 3º cliente: ")
cliente3_idade = int(input("Digite a idade do 3º cliente: "))

#  quartos e seus preços
quartos = ["Simples", "Duplo", "Luxo"]
precos = [100, 150, 250]

# Cliente 1 escolhe o quarto
cliente1_quarto = input(f"{cliente1_nome}, escolha o tipo de quarto (Simples / Duplo / Luxo): ")
if cliente1_quarto == "Simples":
    cliente1_preco = precos[0]
elif cliente1_quarto == "Duplo":
    cliente1_preco = precos[1]
elif cliente1_quarto == "Luxo":
    cliente1_preco = precos[2]
else:
    print("Opção inválida! Será considerado quarto Simples.")
    cliente1_preco = precos[0]

cliente1_dias = int(input(f"Quantos dias {cliente1_nome} ficará hospedado(a)? "))
valor_cliente1 = cliente1_preco * cliente1_dias

# Cliente 2 escolhe o quarto
cliente2_quarto = input(f"{cliente2_nome}, escolha o tipo de quarto (Simples / Duplo / Luxo): ")
if cliente2_quarto == "Simples":
    cliente2_preco = precos[0]
elif cliente2_quarto == "Duplo":
    cliente2_preco = precos[1]
elif cliente2_quarto == "Luxo":
    cliente2_preco = precos[2]
else:
    print("Opção inválida! Será considerado quarto Simples.")
    cliente2_preco = precos[0]

cliente2_dias = int(input(f"Quantos dias {cliente2_nome} ficará hospedado(a)? "))
valor_cliente2 = cliente2_preco * cliente2_dias

# Cliente 3 escolhe o quarto
cliente3_quarto = input(f"{cliente3_nome}, escolha o tipo de quarto (Simples / Duplo / Luxo): ")
if cliente3_quarto == "Simples":
    cliente3_preco = precos[0]
elif cliente3_quarto == "Duplo":
    cliente3_preco = precos[1]
elif cliente3_quarto == "Luxo":
    cliente3_preco = precos[2]
else:
    print("Opção inválida! Será considerado quarto Simples.")
    cliente3_preco = precos[0]

cliente3_dias = int(input(f"Quantos dias {cliente3_nome} ficará hospedado(a)? "))
valor_cliente3 = cliente3_preco * cliente3_dias

# Exibição dos valores finais
print("\n--- RESUMO DAS RESERVAS ---")
print(f"{cliente1_nome} ({cliente1_idade} anos): R$ {valor_cliente1:.2f} ({cliente1_quarto} por {cliente1_dias} dias)")
print(f"{cliente2_nome} ({cliente2_idade} anos): R$ {valor_cliente2:.2f} ({cliente2_quarto} por {cliente2_dias} dias)")
print(f"{cliente3_nome} ({cliente3_idade} anos): R$ {valor_cliente3:.2f} ({cliente3_quarto} por {cliente3_dias} dias)")
