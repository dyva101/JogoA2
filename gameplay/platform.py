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
    """
    Desenha as plataformas na tela.

    Parameters:
    - screen: Tela onde as plataformas serão desenhadas.
    - platform_group (pygame.sprite.Group): Grupo de plataformas.
    """
    platform_group.draw(screen)
    for platform in platform_group:
        pygame.draw.rect(screen, (255, 0, 0), platform.rect, 2)
