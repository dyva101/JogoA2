import pygame as py

class SpriteSheet():
    """
    Classe para auxiliar no recorte de spritesheets
    """

    def __init__(self):
        pass
    def get_image(self, sheet, width, height, scale):
        """
        Pega uma imagem de uma sprite sheet
        :param x: posição x da imagem na sprite sheet
        :param y: posição y da imagem na sprite sheet
        :param width: largura da imagem
        :param height: altura da imagem
        :param scale: define a escala da imagem
        :return: imagem recortada
        """
        image = py.Surface([width, height], py.SRCALPHA, 32).convert_alpha()
        image.blit(sheet, (0, 0), (0, 0, width, height))
        image = py.transform.scale(image, (width * scale, height * scale))

        return image