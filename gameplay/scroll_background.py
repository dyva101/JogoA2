"""
Manutenção do rolamento do cenário    
"""

import math
class ScrollBackground():
    """
    Classe para gerenciar o movimento de fundo (scrolling) na tela.

    Parameters:
    - SCREEN_HEIGHT (int): Altura da tela.
    - screen: Tela onde o fundo será desenhado.
    - scroll (int): Posição de rolagem do fundo.
    - scroll_speed (int): Velocidade de rolagem do fundo.

    """
    def __init__(self, SCREEN_HEIGHT, screen, scroll, scroll_speed, bkgd):
        """Inicializa a classe ScrollBackground

        Parameters:
        - SCREEN_HEIGHT (int): Altura da tela.
        - screen: Tela onde o fundo será desenhado.
        - scroll (int): Posição de rolagem do fundo.
        - scroll_speed (int): Velocidade de rolagem do fundo.
        - bkgd: Imagem de fundo a ser utilizada.
        """
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen = screen
        self.scroll = scroll
        self.scroll_speed = scroll_speed
        self.bkgd = bkgd

    def scroll_bkgd(self):
        """
        Realiza o movimento de rolagem do fundo na tela.

        Returns:
        - int: Nova posição de rolagem do fundo.
        """

        # Fundo em movimento
        height = self.bkgd.get_height()
        
        # Criando tela
        tiles = math.ceil(self.SCREEN_HEIGHT / height) + 1
        
        for i in range(0, tiles):
            self.screen.blit(self.bkgd, (0, -height*i + self.scroll))
        
        self.scroll += self.scroll_speed
        
        if abs(self.scroll) > height:
            self.scroll = 0
        
        return self.scroll