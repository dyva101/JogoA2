import pygame as py

class SpriteSheet():
    """
    Classe para auxiliar no recorte de spritesheets
    """

    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet

    def get_image(self, x, y, width, height, color_key):
        """
        Pega uma imagem de uma sprite sheet
        :param x: posição x da imagem na sprite sheet
        :param y: posição y da imagem na sprite sheet
        :param width: largura da imagem
        :param height: altura da imagem
        :param color_key: cor da imagem que será transparente
        :return: imagem recortada
        """
        # Criando uma imagem vazia
        image = py.Surface([width, height]).convert()

        # Copiando a imagem da sprite sheet
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Setando a cor para ser transparente
        image.set_colorkey(color_key)

        # Retornando a imagem
        return image