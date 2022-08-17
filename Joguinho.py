import pygame
from random import randint  

pygame.init()

x=300  # med 300; max 480; min 120
y=50
pos_x = 145
pos_y1 = 800 #carro esquerdo
pos_y2 = 1350 #carro do meio
pos_y3 = 1000 #carro direito
velocidade = 15
timer = 0
tempo_segundos = 0

fundo = pygame.image.load('fundo.png')
carro = pygame.image.load('carro_roxo.png')
carro1 = pygame.image.load('carro_branco.png')
carro2 = pygame.image.load('carro_preto.png')
carro3 = pygame.image.load('carro_amarelo.png')
policia = pygame.image.load('carro_policia.png')

font = pygame.font.SysFont('ariel black', 25)
texto = font.render("Tempo: "+str(tempo_segundos)+"s", True, (0,0,0),(211,211,211))
pos_texto = texto.get_rect()
pos_texto.center = (50,50)

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Joguinho")

janela_aberta = True
while janela_aberta:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    
    '''if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade'''

    if comandos[pygame.K_LEFT] and x>= 120:
        x-= velocidade
    if comandos[pygame.K_RIGHT] and x<= 480:
        x+= velocidade
    if comandos[pygame.K_DOWN]:
        x=300
        y= 50
        pos_y1 = 800
        pos_y2 = 1350
        pos_y3 = 1000
        timer = 0
        tempo_segundos = 0
        texto = font.render("Tempo: "+str(tempo_segundos)+"s", True, (0,0,0),(211,211,211))

    #detectar colisão
    if x+80 > pos_x+325 and y+180 > pos_y3: #carro direito
        y=1200
    if x-80 < pos_x and y+180 > pos_y1: #carro esquerdo
        y=1200
    if (x+80 > pos_x+155 and y+180 > pos_y2) and (x-80 < pos_x+155 and y+180 > pos_y2): #carro do meio
        y=1200

    pos_y1-= velocidade + 12
    if pos_y1 <= -125:
        pos_y1= randint(800,1500)
    pos_y2-= velocidade + 10
    if pos_y2 <= -125:
        pos_y2= randint(800,1500)
    pos_y3-= velocidade + 11
    if pos_y3 <= -125:
        pos_y3= randint(800,1500)

    # condição para deixar pelo menos 1 espaço pro carro passar garantido
    if pos_y1-pos_y2 <= 400 and pos_y1-pos_y2 >= -400:
        if pos_y2-pos_y3 <= 400 and pos_y2-pos_y3 >= -400:
            if pos_y3-pos_y1<= 400 and pos_y3-pos_y1 >= -400:
                pos_y2+=300
    
    if timer<20: #50ms por rodada, logo 20*50ms = 1000ms = 1s
        timer+=1
    else:
        tempo_segundos+=1
        texto = font.render("Tempo: "+str(tempo_segundos)+"s", True, (0,0,0),(211,211,211))
        timer = 0

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    janela.blit(policia, (pos_x,pos_y1))
    janela.blit(carro1, (pos_x+180,pos_y2))
    janela.blit(carro2, (pos_x+325,pos_y3))
    janela.blit(texto,pos_texto)

    pygame.display.update()

pygame.quit()