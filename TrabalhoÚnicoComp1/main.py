import pygame
from pygame.locals import *
import easygui
from player import Player
from world import World
from creditoworld import CreditoWorld
from var import screen_height, screen_width, default_image_size, small_image_size, TILE_SIZE, world_data, credito_world_data, matrix_dict, world_data2, world_data3
# setup básico
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trabalho de Comp 1")

ufrj_img = pygame.image.load('assets/UFRJ.png')
ufrj_img = pygame.transform.scale(ufrj_img, default_image_size)

global game_state
game_state = "running"

#calculo1
def calculo1(x, y):
    calculo = pygame.image.load('assets/calculo1.png')
    calculo = pygame.transform.scale(calculo, default_image_size)
    rect_calculo = calculo.get_rect()
    rect_calculo.x = x
    rect_calculo.y = y
    screen.blit(calculo, rect_calculo)
    return rect_calculo

def calculo2(x, y):
    calculo2 = pygame.image.load('assets/calculo2.png')
    calculo2 = pygame.transform.scale(calculo2, default_image_size)
    rect_calculo2 = calculo2.get_rect()
    rect_calculo2.x = x
    rect_calculo2.y = y
    screen.blit(calculo2, rect_calculo2)
    return rect_calculo2

def renomear(x, y):
    nome_img = pygame.image.load('assets/nome_img.png')
    nome_img = pygame.transform.scale(nome_img, default_image_size)
    rect_nome_img = nome_img.get_rect()
    rect_nome_img.x = x
    rect_nome_img.y = y
    screen.blit(nome_img, rect_nome_img)
    return rect_nome_img

#dividindo a tela em "tiles" para montar o mundo
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (0, 0, 255), (0, line * TILE_SIZE), (screen_width, line * TILE_SIZE))
		pygame.draw.line(screen, (0, 0, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, screen_height))



player = Player(100, screen_height - 130, game_state)
world = World(world_data)
world2 = World(world_data2)
world3 = World(world_data3)
creditoWorld = CreditoWorld(credito_world_data)
white = (255, 255, 255)
black = (0,0,0)
running = True
calculo1_rect = calculo1(450, 0)
calculo2_rect = calculo2(550, 0)
nome_img_rect = renomear(440, screen_height - 130)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "running":
        # clock determina o "fps" do jogo -- NAO TIRAR!!! DANDO MUITO PROBLEMA -- entender melhor depois
        clock = pygame.time.Clock()
        clock.tick(100)
        screen.fill(white)
        world.draw(screen)
        creditoWorld.draw(screen)
        game_state = player.update(calculo1_rect, world, creditoWorld, screen, game_state, calculo2_rect)
        screen.blit(ufrj_img, (880, 10))
        calculo1_rect = calculo1(450, 50)  # Atualizando a posição do retângulo do objeto calculo1
        nome_img_rect = renomear(650, screen_height - 360)
        pygame.display.update()

    elif game_state == "running2":
        # clock determina o "fps" do jogo -- NAO TIRAR!!! DANDO MUITO PROBLEMA -- entender melhor depois
        clock = pygame.time.Clock()
        clock.tick(100)
        screen.fill(white)
        world2.draw(screen)
        creditoWorld.draw(screen)
        game_state = player.update(calculo2_rect, world2, creditoWorld, screen, game_state, calculo1_rect)
        screen.blit(ufrj_img, (880, 10))
        calculo2_rect = calculo2(550, 50)  # Atualizando a posição do retângulo do objeto calculo1
        pygame.display.update()

    elif game_state == "running3":
        clock = pygame.time.Clock()
        clock.tick(100)
        screen.fill(white)
        world3.draw(screen)
        pygame.display.update()


pygame.quit()
