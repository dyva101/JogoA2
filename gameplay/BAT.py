import pygame as py
import random
import character as char
import scroll_background as bg_gen
import platform as plat
import item
import button as bt
import options as opt
import options_enum as opt_enum
import sprites


class Bat():
    """
    Organização Principal do Jogo
    """

    def __init__(self, height, width):
        self.width = width
        self.height = height
    
    def start(self):
        py.init()

        #Variáveis
        current_time = py.time.get_ticks()
        player_start_x = 0
        player_start_y = 0
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

        #Sonoplastia
        py.mixer.init()
        py.mixer.music.load("assets\TrilhaSonora.mp3")
        py.mixer.music.play(-1)

        #Carregando imagens necessárias
        player_idle = py.image.load("assets\calunio.png").convert_alpha()
        imagem_plataforma = py.image.load("assets\plataforma.png")
        bkgd = py.image.load("assets\imagem_final.jpg").convert()
        
        #Geração de Plataformas
        platform_group = py.sprite.Group()

        # Plataformas temporária
        for p in range(plat.max_plataformas):
            p_2dp = random.randint(80, 150) 

            if p%2 == 0:
                p_x = random.randint(p_2dp, (self.width)/2 - p_2dp)
            else:
                p_x = random.randint(self.width/2 + p_2dp, self.width - p_2dp)
            
            p_y = p * random.randint(int(self.height/ plat.max_plataformas), int(self.height/plat.max_plataformas) + 10)
            plataforma_1 = plat.Plataforma(p_x, p_y, p_2dp, imagem_plataforma)
            platform_group.add(plataforma_1)
            
        # Plataforma Inicial
        start_platform_x = 20
        start_platform_y = self.height - 20
        start_platform = plat.Plataforma(start_platform_x, start_platform_y, 80, imagem_plataforma)
        platform_group.add(start_platform)

        #Criando player
        sprite_player = sprites.SpriteSheet()
        sprite_player = sprite_player.get_image(player_idle, 2000, 1890, 0.4)
        fofo = char.MainPlayer(50, 50 , sprite_player, self.width, self.height, platform_group, GRAVITY)

        #loop principal do jogo
        while game_on:
            clock.tick(60) 
            
            if fofo.rect.bottom > SCREEN_HEIGHT:
                fofo.kill()
                game_on = False
            
            else:
                fofo.move()

            # Gerando Cenário
            BKGD = bg_gen.ScrollBackground(self.height, screen, scroll, 5, bkgd)
            scroll = BKGD.scroll_bkgd()
            plat.draw(screen, platform_group)
            
            #Desenhando o jogador
            fofo.draw(screen)

            for event in py.event.get():
                if event.type == py.QUIT:
                    game_on = False

            py.display.update()