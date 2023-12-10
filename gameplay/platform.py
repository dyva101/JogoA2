"""
Tratamento das plataformas como sprites 
"""

import pygame
import random
import math
import character as char

pygame.init()

max_plataformas = 6

class Plataforma(pygame.sprite.Sprite):
    """Classe geradora das plataformas do jogo

    Parameters:
        
    """
    def __init__(self, x, y, width, imagem_plataforma):
        """Inicializa a classe Plataforma

        Parameters:
            x (int): coordenada-x 
            y (int): coordenada-y
            width (int): largura da plataforma
            imagem_plataforma (png): png da plataforma
        """
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