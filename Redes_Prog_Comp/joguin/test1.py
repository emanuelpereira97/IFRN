import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#Carrega a musica de fundo
musica_de_fundo = pygame.mixer.music.load('./joguin/music/pixel-party-218705.mp3')
#Toca a musica repetidamente
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

# Configurações da tela
pygame.display.set_caption('JogOvo')
largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Cores
preto = (0, 0, 0)
branco = (255,255,255)

# Configurações do Ovo
largura_ovo = 30
altura_ovo = 45
posicao_x_ovo = (largura_tela/2)-(largura_ovo/2)
posicao_y_ovo = (altura_tela/2)-(altura_ovo/2)

# Carrega a imagem como plano de fundo
plano_de_fundo = pygame.image.load('./joguin/imgs/sky.jpg')
plano_de_fundo = pygame.transform.scale(plano_de_fundo, (largura_tela, altura_tela))

# Carrega e ajusta a escala da imagem do Ovo
ovo = pygame.image.load('./joguin/imgs/egg.png')
ovo = pygame.transform.scale(ovo, (100, 100))
mask_ovo = pygame.mask.from_surface(ovo)

# Redimensiona a imagem do ovo para o contador de vidas
ovo_vida = pygame.image.load('./joguin./imgs/ovo_vida.png')
ovo_vida = pygame.transform.scale(ovo_vida, (60, 50))

# Logo do Jogo
logovo = pygame.image.load('./joguin./imgs/Logo.png')
logovo = pygame. transform.scale(logovo, (90,80))

# Variável para o contador de vidas
vidas = 3
tempo_perda_vida = 0  # Variável para armazenar o tempo entre perdas de vida

# Carrega e ajusta a escala de tamanho das Nuvens
# Cria a mascara para a superficie da imagem
# Cria um retangulo usando as dimensões da imagem e o posiciona
nuvem_esq_1 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_esq_1 = pygame.transform.scale(nuvem_esq_1, (350, 200))
mask_nuvem_esq_1 = pygame.mask.from_surface(nuvem_esq_1) 
rect_nuvem_esq_1 = nuvem_esq_1.get_rect(topleft=(-70, 350))

nuvem_dir_1 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_dir_1 = pygame.transform.scale(nuvem_dir_1, (500, 200))
mask_nuvem_dir_1 = pygame.mask.from_surface(nuvem_dir_1)
rect_nuvem_dir_1 = nuvem_dir_1.get_rect(topleft=(250, 320))

nuvem_esq_2 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_esq_2 = pygame.transform.scale(nuvem_esq_2, (400, 200))
mask_nuvem_esq_2 = pygame.mask.from_surface(nuvem_esq_2)
rect_nuvem_esq_2 = nuvem_esq_1.get_rect(topleft=(-70, 500))

nuvem_dir_2 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_dir_2 = pygame.transform.scale(nuvem_dir_2, (400, 200))
mask_nuvem_dir_2 = pygame.mask.from_surface(nuvem_dir_2)
rect_nuvem_dir_2 = nuvem_dir_2.get_rect(topleft=(310, 500))

nuvem_central_1 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_central_1 = pygame.transform.scale(nuvem_central_1, (400, 200))
mask_nuvem_central_1 = pygame.mask.from_surface(nuvem_central_1)
rect_nuvem_central_1 = nuvem_central_1.get_rect(topleft=(100, 700))

nuvem_esq_grande_1 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_esq_grande_1 = pygame.transform.scale(nuvem_esq_grande_1, (600, 200))
mask_nuvem_esq_grande_1 = pygame.mask.from_surface(nuvem_esq_grande_1)
rect_nuvem_esq_grande_1 = nuvem_esq_grande_1.get_rect(topleft=(-150, 900))

nuvem_dir_grande_1 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_dir_grande_1 = pygame.transform.scale(nuvem_dir_grande_1, (500, 200))
mask_nuvem_dir_grande_1 = pygame.mask.from_surface(nuvem_dir_grande_1)
rect_nuvem_dir_grande_1 = nuvem_dir_grande_1.get_rect(topleft=(250, 1200))

nuvem_esq_grande_2 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_esq_grande_2 = pygame.transform.scale(nuvem_esq_grande_2, (450, 200))
mask_nuvem_esq_grande_2 = pygame.mask.from_surface(nuvem_esq_grande_2)
rect_nuvem_esq_grande_2 = nuvem_esq_grande_2.get_rect(topleft=(-150, 140))

nuvem_dir_grande_2 = pygame.image.load('./joguin/imgs/nuvem.png')
nuvem_dir_grande_2 = pygame.transform.scale(nuvem_dir_grande_2, (450, 200))
mask_nuvem_dir_grande_2 = pygame.mask.from_surface(nuvem_dir_grande_2)
rect_nuvem_dir_grande_2 = nuvem_dir_grande_2.get_rect(topleft=(350, 160))

# Controla o incremento na posição da nuvem, usado para fazer a nuvem subir
velocidade_nuvens = 1

# Incrementa 5 na posição do Ovo será usado em X e Y
velocidade_ovo = 5

# Define a fonte para o texto
game_ovo =  pygame.image.load('./joguin/imgs/game_ovo.png')
game_ovo = pygame.transform.scale(game_ovo, (largura_tela,altura_tela))
fonte = pygame.font.SysFont('arial', 40, True, True)

# Contabiliza os pontos, atualiza acada ciclo
pontos = 0

while True:
    clock.tick(25)
    tela.fill((preto))
    
    # Mensagem com os pontos
    mensagem_pontos = f'Pontos: {round(pontos,1)}'
    texto_formatado = fonte.render(mensagem_pontos, False, preto)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Verifica se as vidas acabaram
    if vidas <= 0:
        # Exibe a tela de Game Over
        tela.blit(game_ovo,(0, 0))
        pygame.display.flip()
        pygame.time.delay(4000)  # Espera 3 segundos antes de sair
        pygame.quit()
        exit()

    # Desenha o plano de fundo
    tela.blit(plano_de_fundo, (0, 0))

    # Desenha o ovo
    rect_ovo = ovo.get_rect(topleft=(posicao_x_ovo, posicao_y_ovo))
    tela.blit(ovo, rect_ovo.topleft)

    # Movimentação do ovo com teclado
    if pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]:
        posicao_x_ovo -= velocidade_ovo
    if pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]:
        posicao_x_ovo += velocidade_ovo
    if pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]:
        posicao_y_ovo -= velocidade_ovo
    if pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_s]:
        posicao_y_ovo += velocidade_ovo

    # Lista de nuvens e seus rect
    nuvens = [
        (nuvem_dir_1, rect_nuvem_dir_1),
        (nuvem_esq_1, rect_nuvem_esq_1),
        (nuvem_esq_2, rect_nuvem_esq_2),
        (nuvem_dir_2, rect_nuvem_dir_2),
        (nuvem_central_1, rect_nuvem_central_1),
        (nuvem_esq_grande_1, rect_nuvem_esq_grande_1),
        (nuvem_dir_grande_1, rect_nuvem_dir_grande_1),
        (nuvem_esq_grande_2, rect_nuvem_esq_grande_2),
        (nuvem_dir_grande_2, rect_nuvem_dir_grande_2)
    ]

    # Desenha e movimenta as nuvens verificando o rect(quadrado) e a imagem
    for quadrado, nuvem in nuvens:
        nuvem.y -= velocidade_nuvens
        if nuvem.bottom <= 0:
            nuvem.y = altura_tela
        tela.blit(quadrado, nuvem.topleft)

    # Logo do jogo (LogOvo)
    tela.blit(logovo, ((largura_tela/2) , -10))

    # Mantém o Ovo dentro da tela
    if posicao_x_ovo >= 580:
        posicao_x_ovo = 570
    if posicao_x_ovo <= -45:
        posicao_x_ovo = -35

    # Lista com as mascaras e os rect das nuvens para colisão
    nuvens_mask = [
        (mask_nuvem_dir_1, rect_nuvem_dir_1),
        (mask_nuvem_esq_1, rect_nuvem_esq_1),
        (mask_nuvem_esq_2, rect_nuvem_esq_2),
        (mask_nuvem_dir_2, rect_nuvem_dir_2),
        (mask_nuvem_central_1, rect_nuvem_central_1),
        (mask_nuvem_esq_grande_1, rect_nuvem_esq_grande_1),
        (mask_nuvem_dir_grande_1, rect_nuvem_dir_grande_1),
        (mask_nuvem_esq_grande_2, rect_nuvem_esq_grande_2),
        (mask_nuvem_dir_grande_2, rect_nuvem_dir_grande_2)
    ]
    
    # Verificação de colisão e o tempo entre perder uma vida e outra
    # Se nunca perdeu vida antes ou já passaram 3 segundos (3000 ms) desde a última perda, dimui uma vida

    if tempo_perda_vida == 0 or pygame.time.get_ticks() - tempo_perda_vida >= 3000:
        for mask_nuvem, rect_nuvem in nuvens_mask:
            offset = (rect_nuvem.left - rect_ovo.left, rect_nuvem.top - rect_ovo.top)
            if mask_ovo.overlap(mask_nuvem, offset):
                vidas -= 1
                tempo_perda_vida = pygame.time.get_ticks()  # Registra o tempo atual
            else:
                pontos += 0.25 #incrementa um ponto sempre que não houver colisão

    # Desenha o contador de vidas no canto superior direito
    for i in range(vidas):
        tela.blit(ovo_vida, (largura_tela - 60 - i*60 , 0))  # Exibe os ovos representando vidas

    # Exibe os pontos a cada ciclo
    tela.blit(texto_formatado, (0,0))
    # Atualiza a tela
    pygame.display.flip()
