import pygame
from pygame.locals import *
import easygui
from var import screen_height, screen_width, default_image_size, small_image_size, TILE_SIZE, world_data, credito_world_data

#aplicando o world data (em baixo) no grid do jogo
class World():
    def __init__(self, data):
        self.tile_list = []

        solo_img = pygame.image.load('assets/chao.png')
        grass_img = pygame.image.load('assets/chaocima.png')
        credito_img = pygame.image.load('assets/credito.png')

        fileira = 0
#analisa a world data (criada embaixo) e determina imagens para diferentes números possíveis
        for row in data:
            coluna = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(solo_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    #localiza o tile no grid vv
                    img_rect.x = coluna * TILE_SIZE
                    img_rect.y = fileira * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = coluna * TILE_SIZE
                    img_rect.y = fileira * TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                coluna += 1
            fileira += 1
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
