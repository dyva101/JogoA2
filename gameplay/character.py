import pygame
import math
import random
from pygame.sprite import Group
from abc import ABC, abstractmethod

pygame.init()
jump_fx = pygame.mixer.Sound("imgs and songs/jumpland44100.mp3")

class Character(ABC):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img      

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
        self.isjumping = False

        #variáveis importantes para o player
        self.flip = False
        self.lateral_speed = 10
        self.y_speed = 3

        #Sprites para animações
        """animation_list = []
        sprite_walking_right  = 
        for animation in range(5):
            image_animations_temp = []
            image_animations_temp.append(pygame.image.load("assets/andando_pra_direita.png"))
            self.animation_list.append(pygame.transform.scale(animation, (80, 80)))
        
        for animation in range(5):
            image_animations_temp = []
            image_animations_temp.append(pygame.image.load("assets/andando_pra_direita.png"))
            self.animation_list.append(pygame.transform.scale(animation, (80, 80)))  
        for animation in range(5):
            image_animations_temp = []
            image_animations_temp.append(pygame.image.load("assets/andando_pra_direita.png"))
            self.animation_list.append(pygame.transform.scale(animation, (80, 80)))
        for animation in range(3):
            image_animations_temp = []
            image_animations_temp.append(pygame.image.load("assets/andando_pra_direita.png"))
            self.animation_list.append(pygame.transform.scale(animation, (80, 80)))
        for animation in range(4):
            image_animations_temp = []
            image_animations_temp.append(pygame.image.load("assets/andando_pra_direita.png"))
            self.animation_list.append(pygame.transform.scale(animation, (80, 80)))   
        """
    
    
    
    
    def kill(self):
        pass
        
    def move(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        
        # Movimento lateral
        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.left > 0:
            self.x -= self.lateral_speed
            dx = -10 
            self.flip = True
        if (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right + self.lateral_speed <= self.width:
            self.x += self.lateral_speed
            dx = 10 
            self.flip = False

        # Mecanismo de pulo
        if not self.isjumping and (key[pygame.K_UP] or key[pygame.K_w]):
            self.isjumping = True
            jump_fx.play() 
            dx = -self.rect.left
            self.y_speed = -3

        # Aplicando gravidade e atualizando a posição vertical durante o pulo
        if self.isjumping:
            self.y += self.y_speed
            self.y_speed += self.GRAVITY
            print(self.y_speed)
            dx = SCREEN_WIDTH - self.rect.right
            self.time_counting += 1



    

        #update rectangle position 
        self.rect.x += dx 
        self.rect.y += dy   
            
        
        # Detecção de colisão
        for plataforma in self.platform_group:    
            if pygame.sprite.collide_rect(self, plataforma) and self.y_speed >= 0:
                self.y = plataforma.rect.top
                self.isjumping = False
                self.y_speed = 0
            else:
                self.isjumping = True

        # Atualizando a posição do jogador
        self.rect.center = (self.x, self.y)

    def draw(self, screen):

        flipped_image = pygame.transform.flip(self.imagem, self.flip, False)
        screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    
    def update(self):

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