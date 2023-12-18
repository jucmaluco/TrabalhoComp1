import pygame
from pygame.locals import *
import easygui
from var import screen_height, screen_width, default_image_size, small_image_size, TILE_SIZE, world_data, credito_world_data, matrix_dict
import json

class Player():
    #controi o objeto do player
    def __init__(self, x, y, game_state):
        img = pygame.image.load('assets/Player.png')
        self.image = pygame.transform.scale(img, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumping = False
        self.game_state = game_state
    def update(self, calculo1_rect, world, creditoWorld, screen, game_state, calculo2_rect):
        movex = 0
        movey = 0
        credito_counter = 0
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
        if self.rect.colliderect(calculo1_rect):
            output = easygui.ynbox('Qual a derivada de 8x²?', 'Title', ('16x', '16'))
            if output:
                easygui.msgbox("Boa!", "acertou")
                self.game_state = "running2"
            else:
                easygui.msgbox("Tente novamente!", "errou")
            self.rect.x = 100
            self.rect.y = screen_height - 130
        if self.rect.colliderect(calculo2_rect):
            output = easygui.ynbox('Qual a integral de 2x?', 'Title', ('x²', 'x/2'))
            if output:
                easygui.msgbox("Boa!", "acertou")
                self.game_state = "running3"
            else:
                easygui.msgbox("Tente novamente!", "errou")
            self.rect.x = 100
            self.rect.y = screen_height - 130
        #colisão player-mundo
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
        #colisão player-moeda
        for tile in creditoWorld.tile_list:
            if tile[1].colliderect(self.rect):
                credito_counter += 1
                print(credito_counter)

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
        return self.game_state

