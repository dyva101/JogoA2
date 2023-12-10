import pygame as py
import math
import random
from pygame.sprite import Group
from abc import ABC, abstractmethod

py.init()
jump_fx = py.mixer.Sound("assets\jumpland44100.mp3")
death_fx = py.mixer.Sound("assets\deathsound.mp3")

class Character(ABC):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img      

class MainPlayer(Character):
    def __init__(self, x, y, player_img, SCREEN_WIDTH, SCREEN_HEIGHT, platform_group, GRAVITY):
        super().__init__(x, y, player_img)
        self.player_img = player_img
        self.imagem = py.transform.scale(self.player_img, (80, 80))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.platform_group = platform_group
        self.GRAVITY = -0.03
        self.isjumping = False

        #variáveis importantes para o player
        self.flip = False
        self.lateral_speed = 10
        self.y_speed = -3
    
    def kill(self):
        death_fx.play()
        
    def move(self):
        dx = 0
        dy = 0
        key = py.key.get_pressed()
        
        # Movimento lateral
        if (key[py.K_LEFT] or key[py.K_a]) and self.rect.left > 0:
            dx -= self.lateral_speed
            self.flip = True
        if (key[py.K_RIGHT] or key[py.K_d]) and (self.rect.right + self.lateral_speed) <= self.width:
            dx += self.lateral_speed
            self.flip = False
        
        # Mecanismo de pulo
        if not self.isjumping and (key[py.K_UP] or key[py.K_w]) and (self.rect.top < self.height):
            self.isjumping = True
            jump_fx.play() 
            self.y_speed = -1
        elif self.isjumping:
            self.y_speed -= self.GRAVITY
            dy += self.y_speed

        for platform in self.platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, 800, 756):
                if self.rect.bottom < platform.rect.centery:
                    if self.y_speed > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.y_speed = -3
                
        #update rectangle position
        self.rect.x += dx 
        self.rect.y += dy   
        

    def draw(self, screen):

        flipped_image = py.transform.flip(self.imagem, self.flip, False)
        screen.blit(flipped_image, self.rect)
        py.draw.rect(screen, (255, 0, 0), self.rect, 2)
    
    def update(self):
        pass

class Enemy(ABC):
    def __init__(self, x, y, enemy_img):
        self.x = x
        self.y = y
        self.enemy_img = enemy_img
        self.imagem = py.transform.scale(self.enemy_img, (100, 100))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 10
    
        
    def draw(self, screen):
        screen.blit(self.imagem, self.rect)
        py.draw.rect(screen, (255, 0, 0), self.rect, 2)
        
class professor(Enemy):
    def __init__(self, x, y, enemy_img):
        super().__init__(x, y, enemy_img)
        self.speed = 5
        self.health = 100

    def throw_evaluation(self):
        pass
    
    def throw_chalk(self):
        pass