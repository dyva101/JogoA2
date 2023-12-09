import pygame as py
import character as char
import scroll_background as bg_gen
import platform as plat
import item
import button as bt
import options as opt
import options_enum as opt_enum


class Bat():
    """
    Organização Principal do Jogo
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def start(self):
        py.init()

        #Variáveis
        current_time = py.time.get_ticks()
        SCREEEN_WIDTH = self.width
        SCREEN_HEIGHT = self.height
        last_update = py.time.get_ticks()
        clock = py.time.Clock() # FPS
        animation_cooldonw = 500
        isjumping = False
        time_counting = 0
        game_on = True
        scroll = 0
        GRAVITY = 0.03
        action = 0
        frame = 0

        # Criando uma tela
        screen = py.display.set_mode((self.width, self.height))
        py.display.set_caption("BAT: Uma Perigosa Jornada Universitária")

        #Criando player
        fofo = char.Main_player(player_start_x, player_start_y , idle_1, SCREEN_WIDTH, SCREEN_HEIGHT, platform_group, GRAVITY)

        #Carregando imagens necessárias
        player_idle = py.image.load("imgs and songs/calunio.png").convert_alpha()
        sprite_sheet = sp.SpriteSheet(player_idle)
        imagem_plataforma = py.image.load("imgs and songs/2dplatform.png")
        bkgd = py.image.load("imgs and songs/total_bkgd.png").convert()     

        #loop principal do jogo
        while game_on:
            clock.tick(60) 
            
            if fofo.rect.bottom > SCREEN_HEIGHT:
                fofo.kill()
                game_on = False
            
            else:
                fofo.move()

            # Gerando fundo e plataformas
            new_scroll = bg_gen.scroll_bkgd(SCREEN_HEIGHT, screen, scroll, bkgd)
            scroll = new_scroll
            platform.draw(screen, platform_group)
            
            #Desenhando o jogador
            fofo.draw(screen)
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    game_on = False

            py.display.update()
    
    def finish():
        pass