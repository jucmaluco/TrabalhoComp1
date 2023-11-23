import pygame
from pygame.locals import *
import easygui
from player import Player
from world import World
from creditoworld import CreditoWorld
from var import screen_height, screen_width, default_image_size, small_image_size, TILE_SIZE, world_data, credito_world_data
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


#dividindo a tela em "tiles" para montar o mundo
def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (0, 0, 255), (0, line * TILE_SIZE), (screen_width, line * TILE_SIZE))
		pygame.draw.line(screen, (0, 0, 255), (line * TILE_SIZE, 0), (line * TILE_SIZE, screen_height))



player = Player(100, screen_height - 130)
world = World(world_data)
creditoWorld = CreditoWorld(credito_world_data)
white = (255, 255, 255)
black = (0,0,0)
running = True
calculo1_rect = calculo1(450, 0)


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
        player.update(calculo1_rect, world, creditoWorld, screen)
        screen.blit(ufrj_img, (880, 10))
        calculo1_rect = calculo1(450, 50)  # Atualizando a posição do retângulo do objeto calculo1
        pygame.display.update()

    elif game_state == "running2":
        # clock determina o "fps" do jogo -- NAO TIRAR!!! DANDO MUITO PROBLEMA -- entender melhor depois
        clock = pygame.time.Clock()
        clock.tick(100)
        screen.fill(black)
        player.update(calculo1_rect, world, creditoWorld, screen)
        screen.blit(ufrj_img, (880, 10))
        pygame.display.update()

    elif game_state == "main_menu":
        menu_screen.fill(white)
        menu_screen.blit(ufrj_img, (880, 10))
        pygame.display.update()
pygame.quit()
