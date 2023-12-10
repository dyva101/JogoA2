import pygame as py
import math
import random
from pygame.sprite import Group
from abc import ABC, abstractmethod
import sprites
import menu
import item

py.init()
py.mixer.init()
jump_fx = py.mixer.Sound("assets\\jumpland44100.mp3")
death_fx = py.mixer.Sound("assets\\deathsound.mp3")
CollectPowerup = py.mixer.Sound("assets\\CollectPowerup.mp3")


class Character(ABC):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    @abstractmethod
    def draw(self, screen):
        pass      

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
        self.GRAVITY = 0.025
        self.isjumping = False

        #variáveis importantes para o player
        self.flip = False
        self.lateral_speed = 10
        self.y_speed = -3
    
    def kill(self, death_fx):
        py.mixer.music.set_volume(1)
        death_fx.play()
        py.time.delay(1000)
        py.mixer.music.stop()

        screen = py.display.set_mode((self.width, self.height))

        # Game Over (variáveis)
        game_over_image = py.image.load("assets\menu_image.png").convert_alpha()
        title_image = py.image.load("assets\game_over_image.png").convert_alpha()
        game_over_image = py.transform.scale(game_over_image, (self.width, self.height))
        title_image = py.transform.scale(title_image, (self.width, 200))
        FPS = 60
        BLUE = (0, 0, 255)
        WHITE = (255, 255, 255)

        # Menu
        menu.game_over(screen, game_over_image, title_image, FPS, self.width, self.height, WHITE, BLUE)
            

    def move(self, group_de_inimigos, expresso_group):

        key = py.key.get_pressed()
        
        # Movimento lateral
        if (key[py.K_LEFT] or key[py.K_a]) and self.rect.left > 0:
            self.x -= self.lateral_speed
            self.flip = True
        if (key[py.K_RIGHT] or key[py.K_d]) and self.rect.right + self.lateral_speed <= self.width:
            self.x += self.lateral_speed
            self.flip = False

        # Mecanismo de pulo
        if not self.isjumping and (key[py.K_UP] or key[py.K_w]):
            self.isjumping = True
            jump_fx.play()
            self.y_speed = -3

        # Aplicando gravidade e atualizando a posição vertical durante o pulo
        if self.isjumping:
            self.y += self.y_speed
            self.y_speed += self.GRAVITY
            print(self.y_speed)
        
        # Detector de colisão com inimigos
        for inimigo in group_de_inimigos:
            if py.sprite.collide_rect(self, inimigo):
                self.kill(death_fx)
                py.time.delay(2000)

        for expresso in expresso_group:
            if py.sprite.collide_rect(self, expresso):
                py.mixer.music.set_volume(1)
                CollectPowerup.play()
                expresso.apply_effect(self)

                
            
        # Detecção de colisão
        for plataforma in self.platform_group:
            if self.y_speed >= 0:
                pass

            if py.sprite.collide_rect(self, plataforma):
                pass
                
            if py.sprite.collide_rect(self, plataforma) and self.y_speed > 0:
                self.y = plataforma.rect.top
                self.isjumping = False
                self.y_speed = 0
            else:
                self.y += self.y_speed
                self.y_speed += self.GRAVITY
                

        # Atualizando a posição do jogador
        self.rect.center = (self.x, self.y)
    def draw(self, screen):

        flipped_image = py.transform.flip(self.imagem, self.flip, False)
        screen.blit(flipped_image, self.rect)
    
    def update(self):
        pass

class Enemy(py.sprite.Sprite):  # Removendo a herança ABC e utilizando apenas Sprite
    def __init__(self, x, y, enemy_img, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.x = x
        self.y = y
        self.enemy_img = enemy_img
        self.imagem = py.transform.scale(self.enemy_img, (100, 100))
        self.rect = self.imagem.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 10
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
    
    def draw(self, screen):
        screen.blit(self.imagem, self.rect)
        py.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Professor(Enemy):
    def __init__(self, x, y, enemy_img, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__(x, y, enemy_img, SCREEN_WIDTH, SCREEN_HEIGHT)
        enemy_idle = py.image.load(r"assets\vilao.png").convert_alpha()
        sprite_enemy = sprites.SpriteSheet()
        self.image = sprite_enemy.get_image(enemy_idle, 1600, 1600, 0.09)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self):
        if self.rect.y >= self.height:
            self.kill()

    def throw_evaluation(self):
        pass
    
    def throw_chalk(self):
        pass