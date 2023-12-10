"""
Criação dos itens que formam o jogo
"""
import pygame as py
import sprites

class Item(py.sprite.Sprite):
    """
    Classe para representar um item no jogo

    Parameters:
        x (int): A coordenada x inicial do item.
        y (int): A coordenada y inicial do item.
        item_img (Surface): A imagem do item.
        SCREEN_WIDTH (int): A largura da tela do jogo.
        SCREEN_HEIGHT (int): A altura da tela do jogo.
    Methods:
        update: Identifica quando o sprite deve desaparecer
        apply_effect: aplica os efeitos do powerup
    """
    def __init__(self, x, y, item_img, SCREEN_WIDTH, SCREEN_HEIGHT):
        """Inicializa a classe Item

        Parameters:
            x (int): coordenada-x 
            y (int): coordenada-y
            item_img (png): png do item
            SCREEN_WIDTH (int): largura da tela
            SCREEN_HEIGHT (int): altura da tela
        """
        py.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.item_img = item_img
        expresso_idle = py.image.load(r"assets\expresso.png").convert_alpha()
        sprite_item = sprites.SpriteSheet()
        self.image = sprite_item.get_image(expresso_idle, 1600, 1600, 0.05)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self):
        """
        Atualiza a posição do item e verifica se atingiu a parte inferior da tela para removê-lo.
        """
        if self.rect.y >= self.height:
            self.kill()

    def apply_effect(self, player):
        """
        Aplica o efeito do item ao jogador.

        Parameters:
            player (MainPlayer): O jogador ao qual o efeito será aplicado.
        """
        player.y_speed = -4
        player.image = py.image.load(r"assets\fogo.png").convert_alpha()
        player.image = py.transform.scale(self.image, (80, 80))