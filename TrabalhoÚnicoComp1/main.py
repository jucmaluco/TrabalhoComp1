import pygame
from pygame.locals import *
import easygui
from player import Player
from world import World
from creditoworld import CreditoWorld
from var import screen_height, screen_width, default_image_size, small_image_size, TILE_SIZE, world_data, credito_world_data, matrix_dict, world_data2, world_data3
import json
# setup básico
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
menu_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Trabalho de Comp 1")

ufrj_img = pygame.image.load('assets/UFRJ.png')
ufrj_img = pygame.transform.scale(ufrj_img, default_image_size)

global game_state
game_state = "running"
def carregar_nome():
    try:
        with open('nome_jogador.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados.get("nome", "")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return ""

def salvar_nome(nome):
    with open('nome_jogador.json', 'w') as arquivo:
        json.dump({"nome": nome}, arquivo)

def exibir_nome_do_jogador():
    nome_do_jogador = carregar_nome() if carregar_nome() else "Sem nome"
    easygui.msgbox(f"Bem vindo ao jogo, {nome_do_jogador}", title="Informação do Jogador")

def renomear_jogador():
    novo_nome = easygui.enterbox("Digite seu nome:", title="Nome do Jogador", default=carregar_nome())
    if novo_nome:
        salvar_nome(novo_nome)

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

exibir_nome_do_jogador()
renomear_jogador()

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
