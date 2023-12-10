"""
Tratamento dos sprites para o jogo
"""
import pygame as py

class SpriteSheet():
    """
    Classe para auxiliar no recorte de spritesheets.
    """

    def __init__(self):
        pass
    def get_image(self, sheet, width, height, scale):
        """
        Obtém uma imagem de uma spritesheet.

        Parameters:
        - sheet: Imagem da spritesheet.
        - width (int): Largura da imagem na spritesheet.
        - height (int): Altura da imagem na spritesheet.
        - scale (float): Escala da imagem.

        Returns:
        - pygame.Surface: Imagem recortada e redimensionada.
        """
        image = py.Surface([width, height], py.SRCALPHA, 32).convert_alpha()
        image.blit(sheet, (0, 0), (0, 0, width, height))
        image = py.transform.scale(image, (width * scale, height * scale))

        return image