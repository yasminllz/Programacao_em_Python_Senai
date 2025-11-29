# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/
# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma defini a aaltura a outra a largura 
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))   # define a altura e largura da janela
pygame.display.set_caption("Labirinto")    #titulo do jogo                         

# variavel que atribui cores 
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# defini do tamanho da celula 
tamanho_celula = 40
labirinto = [                                       # uma lista onde define o o desenho do mapa
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],                  #lista biomidimencional
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# duas variveis onde poe posição nas celulas
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40    # variavel define a velocidade 

def desenhar_labirinto():            # criação da função desenhar_labirinto 
    for linha in range(len(labirinto)):         # leitura da linha do labirinto 
        for coluna in range(len(labirinto[linha])):      # leitura da coluna do labirinto com a linha
            cor = preto if labirinto[linha][coluna] == 1 else branco          # Se 1 e  preta se não e branco 
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))      # criando um retangulo pintando cada quadrado

# loop inicial
executando = True
while executando:  #estrutura que define loop infinito
    for evento in pygame.event.get():        # estrutura fluxo de controle, que define os eventos 
        if evento.type == pygame.QUIT:             # 
            executando = False                     # variavel que retorna no false caso o evento seja QUIT


 # lista,  atribuido a ela todos os possiveis eventos no teclado 
    teclas = pygame.key.get_pressed()
    # estrutura de fluxo de controle, verifica se a seta da esqueda
    # foi clicada 
    if teclas[pygame.K_LEFT]:
        # 1 variável que declara dentro da condicional, velocidadepara esquerda 
        novo_x = x - velocidade
        # estrtura de fluxo de controle que defini as posições do personagem
        # defini que anda pelo 0
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x

     # estrtura de fluxo de controle que defini as posições do personagem
     # defini que anda pelo 0        
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
   
     # estrtura de fluxo de controle que defini as posições do personagem
    # defini que anda pelo 0
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    # estrtura de fluxo de controle que defini as posições do personagem
    # defini que anda pelo 0        
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

   

    tela.fill(branco)

    # função chamada desenhar_labirinto 
    desenhar_labirinto()
    # modulo pygame.submodulo draw, desenho do personagem vermelho
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # modulo pygame.submodulo display(tela), atauliza
    pygame.display.flip()

    # modulo pygame.submodulo time, definir a velocidade fps  
    pygame.time.Clock().tick(10)

    pygame.quit()   # modulo pygame com o metodo quit -  fechar o pygame




