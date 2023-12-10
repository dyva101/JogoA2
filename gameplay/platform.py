import pygame
import random
import math
import character as char

pygame.init()

max_plataformas = 6

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, width, imagem_plataforma):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(imagem_plataforma, (width, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.imagem_plataforma = imagem_plataforma

def draw(screen, platform_group):
    platform_group.draw(screen)