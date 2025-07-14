import pygame
import random
import os

# Inicialização
pygame.init()
pygame.mixer.init()

# Tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (50, 153, 213)

# Assets
tamanho_bloco = 20
cobra_img = pygame.image.load(os.path.join("assets", "cobra.png"))
comida_img = pygame.image.load(os.path.join("assets", "comida.png"))
cobra_img = pygame.transform.scale(cobra_img, (tamanho_bloco, tamanho_bloco))
comida_img = pygame.transform.scale(comida_img, (tamanho_bloco, tamanho_bloco))

som_comer = pygame.mixer.Sound(os.path.join("assets", "som_comer.wav"))
som_morte = pygame.mixer.Sound(os.path.join("assets", "som_morte.wav"))

# Fonte
fonte = pygame.font.SysFont("arial", 25)

# Funções
def mensagem(msg, cor, y=altura // 2):
    texto = fonte.render(msg, True, cor)
    ret = texto.get_rect(center=(largura // 2, y))
    tela.blit(texto, ret)

def desenhar_cobra(lista):
    for i, segmento in enumerate(lista):
        if i == len(lista) - 1:
            tela.blit(cobra_img, segmento)
        else:
            pygame.draw.rect(tela, preto, (*segmento, tamanho_bloco, tamanho_bloco))

def menu_inicial():
    while True:
        tela.fill(azul)
        mensagem("Jogo da Cobrinha", preto, y=120)
        mensagem("Pressione ENTER para jogar ou ESC para sair", preto, y=180)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

def jogo():
    x = largura // 2
    y = altura // 2
    x_mudar = tamanho_bloco
    y_mudar = 0

    cobra = []
    comprimento = 1

    comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
    comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)

    relogio = pygame.time.Clock()
    game_over = False

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                tecla = evento.key
                if tecla in [pygame.K_LEFT, pygame.K_a] and x_mudar == 0:
                    x_mudar = -tamanho_bloco
                    y_mudar = 0
                elif tecla in [pygame.K_RIGHT, pygame.K_d] and x_mudar == 0:
                    x_mudar = tamanho_bloco
                    y_mudar = 0
                elif tecla in [pygame.K_UP, pygame.K_w] and y_mudar == 0:
                    y_mudar = -tamanho_bloco
                    x_mudar = 0
                elif tecla in [pygame.K_DOWN, pygame.K_s] and y_mudar == 0:
                    y_mudar = tamanho_bloco
                    x_mudar = 0


        x += x_mudar
        y += y_mudar

        if x < 0 or x >= largura or y < 0 or y >= altura:
            som_morte.play()
            break

        tela.fill(azul)
        tela.blit(comida_img, (comida_x, comida_y))

        cabeca = [x, y]
        cobra.append(cabeca)
        if len(cobra) > comprimento:
            del cobra[0]

        for parte in cobra[:-1]:
            if parte == cabeca:
                som_morte.play()
                game_over = True

        desenhar_cobra(cobra)
        mensagem(f"Pontos: {comprimento - 1}", preto, y=20)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
            comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)
            comprimento += 1
            som_comer.play()

        relogio.tick(15)

    tela.fill(branco)
    mensagem("Você perdeu! Pressione R para reiniciar ou ESC para sair", preto)
    pygame.display.update()
    esperar_gameover()

def esperar_gameover():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    jogo()
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

# Início
menu_inicial()
jogo()
