import pygame
import math
import random
from pygame.sprite import Group
from game_initializer import game_initializer as game_init
from abc import ABC, abstractmethod
from pygame import mixer
import plataforma as plat
from BAT import Bat

pygame.init()
jump_fx = pygame.mixer.Sound("imgs and songs/jumpland44100.mp3")

class Character(ABC):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    
    def get_x(self):
        self.x = _x
        return _x        

class MainPlayer(Character):
    def __init__(self, x, y, player_img, SCREEN_WIDTH, SCREEN_HEIGHT, platform_group, GRAVITY):
        super().__init__(x, y, player_img)
        self.imagem = pygame.transform.scale(self.player_img, (80, 80))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.platform_group = platform_group
        self.GRAVITY = GRAVITY

        #variáveis importantes para o player
        self.flip = False
        self.lateral_speed = 10
        self.y_speed = 3
    

    def move(self):
        if self.rect.bottom > self.height:
            Bat.game_on = False

        else:
            key = pygame.key.get_pressed()
            
            # Movimento lateral
            if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.left > 0:
                self.x -= self.lateral_speed
                self.flip = True
            if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right + self.lateral_speed <= self.width:
                self.x += self.lateral_speed
                self.flip = False

            # Mecanismo de pulo
            if not isjumping and (key[pygame.K_UP] or key[pygame.K_w]):
                game_init.isjumping = True
                jump_fx.play() 
                self.y_speed = -3

            # Aplicando gravidade e atualizando a posição vertical durante o pulo
            if game_init.isjumping:
                self.y += self.y_speed
                self.y_speed += self.GRAVITY
                print(self.y_speed)
                game_init.time_counting += 1
                
            
            # Detecção de colisão
            for plataforma in self.platform_group:
                if self.y_speed >= 0:
                    pass

                if pygame.sprite.collide_rect(self, plataforma):
                    pass
                    
                if pygame.sprite.collide_rect(self, plataforma) and self.y_speed >= 0:
                    self.y = plataforma.rect.top
                    game_init.isjumping = False
                    self.y_speed = 0
                else:
                    self.y += self.y_speed
                    self.y_speed += self.GRAVITY
                    

            # Atualizando a posição do jogador
            self.rect.center = (self.x, self.y)

    def draw(self, screen):
        BLACK = (0, 0, 0)
        animation_list = []
        animation_steps = [5]
        step_counter = 0
        
        for animation in animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(game_init.sprite_sheet.get_image(step_counter, 100, 100, 3, BLACK))
                step_counter += 1
            animation_list.append(temp_img_list)
        
            if current_time - last_update >= animation_cooldonw:
                frame += 1
            last_update = current_time
            if frame >= len(animation_list[action]):
                frame = 0
        
        screen.blit(animation_list[action][frame],(100, 100))

        flipped_image = pygame.transform.flip(self.imagem, self.flip, False)
        screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Enemy(ABC):
    def __init__(self, x, y, enemy_img):
        self.x = x
        self.y = y
        self.enemy_img = enemy_img
        self.imagem = pygame.transform.scale(self.enemy_img, (100, 100))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 10
    
        
    def draw(self, screen):
        screen.blit(self.imagem, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
class professor(Enemy):
    def __init__(self, x, y, enemy_img):
        super().__init__(x, y, enemy_img)
        self.speed = 5
        self.health = 100

    def throw_evaluation(self):
        pass
    
    def throw_chalk(self):
        pass