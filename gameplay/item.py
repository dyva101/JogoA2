import pygame as py
import sprites

class Item(py.sprite.Sprite):
    def __init__(self, x, y, item_img, SCREEN_WIDTH, SCREEN_HEIGHT):
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
        if self.rect.y >= self.height:
            self.kill()

    def apply_effect(self, player):
        player.y_speed = -4
        player.image = py.image.load(r"assets\fogo.png").convert_alpha()
        player.image = py.transform.scale(self.image, (80, 80))