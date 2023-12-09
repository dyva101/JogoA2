import math
class ScrollBackground():
    def __init__(self, SCREEN_HEIGHT, screen, scroll, scroll_speed, bkgd):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen = screen
        self.scroll = scroll
        self.scroll_speed = scroll_speed
        self.bkgd = bkgd

def scroll_bkgd(self):

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