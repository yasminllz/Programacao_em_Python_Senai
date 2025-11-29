
import os
import shutil


# 1. Criar e ler um arquivo 

# cria
with open('arquivo.txt', 'w') as arq:
    arq.write("olá fui criado pelo python.")

# Lê 
with open('arquivo.txt', 'r') as arq:
    print("Conteúdo do arquivo.txt:")
    print(arq.read())



# 2. Criar um diretório

if not os.path.exists('diretorio_exemplo'):
    os.mkdir('diretorio_exemplo')
    print("Diretório criado: diretorio_exemplo")



# 3. Renomear um diretório

if os.path.exists('diretorio_exemplo'):
    os.rename('diretorio_exemplo', 'diretorio_renomeado')
    print("Diretório renomeado para: diretorio_renomeado")



# 4. Listar arquivos em um diretório

print("\nArquivos no diretório renomeado:")
with os.scandir('diretorio_renomeado') as entrada:
    for item in entrada:
        print(item.name)



# 5. Copiar arquivos ou diretórios

# Copiar arquivo
shutil.copy('arquivo.txt', 'diretorio_renomeado/arquivo_copiado.txt')
print("\nArquivo copiado para diretorio_renomeado")

# Copiar diretório 
if os.path.exists('diretorio_renomeado'):
    if not os.path.exists('diretorio_copia'):
        shutil.copytree('diretorio_renomeado', 'diretorio_copia')
        print("Diretório copiado para: diretorio_copia")



# 6. Remover

# Remove arquio
if os.path.exists('arquivo.txt'):
    os.remove('arquivo.txt')
    print("arquivo.txt removido.")

# Remove diretório 
if os.path.exists('diretorio_copia'):
    shutil.rmtree('diretorio_copia')
    print("diretorio_copia removido.")
# ----------------------------------------- junto com a professora ---------------------------------------
    # **Exercício 1: Criar e ler um Arquivo**
import os
import shutil


# with open('teste.txt','r') as arq:
#     c  =  arq.read()
#     print(c)



# **Exemplo 2: Cria um Diretório**



# os.mkdir('nova_pasta')



# **Exercício 3: Renomear um Diretório**



# os.rename('novo_mome', 'novo_nome')



# **Exercício 4:  Listar Arquivos em um Diretório**


# with os.scandir('C:/Users/Aluno/Downloads/Nova pasta/novo_nome') as scann:
#     for sca in scann:
#         print(sca.name)



# **Exercício 5:  Copiar Arquivos em um Diretório**


# shutil.copytree('novo_nome', 'copia')


# **Exercício 6:  Remover**


# shutil.rmtree('copia')