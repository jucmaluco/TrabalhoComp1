import pygame
from pygame.locals import *
import easygui
# setup básico
pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trabalho de Comp 1")
tile_size = 50

#imgufrj
default_image_size = (100, 100)
ufrj_img = pygame.image.load('assets/UFRJ.png')
ufrj_img = pygame.transform.scale(ufrj_img, default_image_size)

def calculo1(x, y):
    calculo = pygame.image.load('assets/calculo1.png')
    calculo = pygame.transform.scale(calculo, default_image_size)
    rect_calculo = calculo.get_rect()
    rect_calculo.x = x
    rect_calculo.y = y
    screen.blit(calculo, rect_calculo)
    return rect_calculo

class Player():
    #controi o objeto do player
    def __init__(self, x, y):
        img = pygame.image.load('assets/Player.png')
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumping = False
    def update(self):
        movex = 0
        movey = 0

        key = pygame.key.get_pressed()
#pulo
        if key[pygame.K_SPACE]  and self.jumping == False and self.is_jumping == False:
            self.vel_y = -20
            self.jumping = True
        if key[pygame.K_SPACE] == False:
            self.jumping = False
#movimento em X
        if key[pygame.K_a]:
            movex -= 10
        if key[pygame.K_d]:
            movex += 10
#gravidade
        self.vel_y += 1
        if self.vel_y > 30:
            self.vel_y = 30
        movey += self.vel_y
#colisão player-calculo1
        if player.rect.colliderect(calculo1_rect):
            easygui.ynbox('Qual a derivada de 8x²?', 'Title', ('16x', '16'))
#colisão
        self.is_jumping = True
        for tile in world.tile_list:
            #Colisão no eixo X:
            if tile[1].colliderect(self.rect.x + movex, self.rect.y, self.width, self.height):
                movex = 0
            #Colisão no eixo y:
            if tile[1].colliderect(self.rect.x, self.rect.y + movey, self.width, self.height):
                #colidindo por baixo (pulando)
                if self.vel_y < 0:
                    movey = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                #colidindo por cima (caindo)
                elif self.vel_y >= 0:
                    movey = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.is_jumping = False
        self.rect.x += movex
        self.rect.y += movey
#impede que o player saia da tela
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            movey = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            movex = 0
        if self.rect.left < 0:
            self.rect.left = 0
            movex = 0
        screen.blit(self.image, self.rect)

#dividindo a tela em "tiles" para montar o mundo
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (0, 0, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (0, 0, 255), (line * tile_size, 0), (line * tile_size, screen_height))
#aplicando o world data (em baixo) no grid do jogo
class World():
    def __init__(self, data):
        self.tile_list = []

        solo_img = pygame.image.load('assets/chao.png')
        grass_img = pygame.image.load('assets/chaocima.png')
        fileira = 0
#analisa a world data (criada embaixo) e determina imagens para diferentes números possíveis
        for row in data:
            coluna = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(solo_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    #localiza o tile no grid vv
                    img_rect.x = coluna * tile_size
                    img_rect.y = fileira * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = coluna * tile_size
                    img_rect.y = fileira * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                coluna += 1
            fileira += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
player = Player(100, screen_height - 130)
world = World(world_data)
white = (255, 255, 255)
running = True
calculo1_rect = calculo1(450, 0)  # Exemplo de posição para o objeto calculo1
while running:
    #clock determina o "fps" do jogo -- NAO TIRAR!!! DANDO MUITO PROBLEMA -- entender melhor depois
    clock = pygame.time.Clock()
    clock.tick(100)
    screen.fill(white)
    world.draw()
    player.update()
    screen.blit(ufrj_img, (880, 10))

    calculo1_rect = calculo1(450, 50)  # Atualizando a posição do retângulo do objeto calculo1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
