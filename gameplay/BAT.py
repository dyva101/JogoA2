"""
Organização do tratamento de eventos do Jogo
"""

import pygame as py
import random
import character as char
import scroll_background as bg_gen
import platform as plat
import item
import sprites
import menu


class Bat:
    """
    Classe principal do jogo.
    """

    def __init__(self, height, width):
        """
        Inicializa a instância da classe Bat.

        Parameters:
        - height (int): Altura da tela do jogo.
        - width (int): Largura da tela do jogo.
        """
        self.width = width
        self.height = height

    def start(self):
        """
        Método principal que inicia o jogo.
        """
        py.init()
        screen = py.display.set_mode((self.width, self.height))

        # Telas (Variáveis)
        menu_image = py.image.load("assets\menu_image.png").convert_alpha()
        title_image = py.image.load(r"assets\title.png").convert_alpha()
        menu_image = py.transform.scale(menu_image, (self.width, self.height))
        title_image = py.transform.scale(title_image, (self.width, 200))
        you_won_image = py.image.load("assets\you_won.png").convert_alpha()
        you_won_image = py.transform.scale(you_won_image, (self.width, 200))
        FPS = 60
        BLUE = (0, 0, 255)
        WHITE = (255, 255, 255)

        # Menu
        menu.main_menu(screen, menu_image, title_image, FPS, self.width, self.height, WHITE, BLUE)
        
        # Variáveis
        current_time = py.time.get_ticks()
        player_start_x = 0
        player_start_y = 0
        SCREEN_WIDTH = self.width  # Corrigindo o nome da variável
        SCREEN_HEIGHT = self.height
        last_update = py.time.get_ticks()
        clock = py.time.Clock()  # FPS
        game_on = True
        scroll = 0
        GRAVITY = 0.03

        # Criando uma tela
        screen = py.display.set_mode((self.width, self.height))
        py.display.set_caption("BAT: Uma Perigosa Jornada Universitária")

        # Sonoplastia
        py.mixer.init()
        py.mixer.music.load("assets\\TrilhaSonora.mp3")
        py.mixer.music.set_volume(0.3)
        py.mixer.music.play(-1)
        jump_fx = py.mixer.Sound("assets\\jumpland44100.mp3")
        death_fx = py.mixer.Sound("assets\\deathsound.mp3")

        #Carregando imagens necessárias
        sprite_expresso = sprites.SpriteSheet()
        imagem_expresso = sprite_expresso.get_image(py.image.load(r"assets\expresso.png").convert_alpha(), 1600, 1600, 0.09)
        imagem_expresso = py.transform.scale(imagem_expresso, (30, 30))
        player_idle = py.image.load("assets\calunio.png").convert_alpha()
        imagem_plataforma = py.image.load("assets\plataforma.png")
        bkgd = py.image.load("assets\imagem_final.jpg").convert()
        enemy_idle = py.image.load(r"assets\vilao.png").convert_alpha()
        sprite_enemy = sprites.SpriteSheet()
        sprite_enemy = sprite_enemy.get_image(enemy_idle, 1600, 1600, 0.09)
        
        #Geração de Plataformas
        platform_group = py.sprite.Group()
        group_de_inimigos = py.sprite.Group()
        expresso_group = py.sprite.Group()

        def generate_new_platform(platform_group, SCREEN_WIDTH, SCREEN_HEIGHT, imagem_plataforma):
            """
            Gera uma nova plataforma aleatória e a adiciona ao grupo de plataformas.

            Parameters:
            - platform_group (pygame.sprite.Group): Grupo de plataformas.
            - SCREEN_WIDTH (int): Largura da tela.
            - SCREEN_HEIGHT (int): Altura da tela.
            - imagem_plataforma: Imagem da plataforma.

            Returns:
            - platform_group (pygame.sprite.Group): Grupo de plataformas atualizado.
            """
            p_size = random.randint(70, 140)
            p_x = random.randint(0, SCREEN_WIDTH - p_size)
            p_size = random.randint(80, 150)
            p_x = random.randint(int(SCREEN_WIDTH/4), int(SCREEN_WIDTH * 4/5))
            p_y = 0

            new_platform = plat.Plataforma(p_x, p_y, p_size, imagem_plataforma)
            platform_group.add(new_platform)

            return platform_group

        #Geração de Plataformas
        platform_group = py.sprite.Group()
        group_de_inimigos = py.sprite.Group()
        
        # Plataformas temporárias
        for p in range(plat.max_plataformas):
            p_2dp = random.randint(80, 150)

            if p % 2 == 0:
                # Posiciona as plataformas mais à esquerda, mas ainda no centro
                p_x = random.randint(int(self.width / 4), int(self.width / 2) - p_2dp)
            else:
                # Posiciona as plataformas mais à direita, mas ainda no centro
                p_x = random.randint(int(self.width / 2), int(self.width * 3 / 4) - p_2dp)

            # Gera coordenadas y aleatórias para as plataformas
            p_y = p * random.randint(int(self.height / plat.max_plataformas), int(self.height / plat.max_plataformas) + 10)

            # Cria a plataforma com as coordenadas geradas
            plataforma_1 = plat.Plataforma(p_x, p_y, p_2dp, imagem_plataforma)
            platform_group.add(plataforma_1)

        # Plataforma Inicial
        start_platform_x = 10
        start_platform_y = self.height - 200
        start_platform = plat.Plataforma(start_platform_x, start_platform_y, 80, imagem_plataforma)
        platform_group.add(start_platform)
        player_start_x = start_platform.rect.centerx - 40
        player_start_y = start_platform.rect.top - 80

        # Criando player
        sprite_player = sprites.SpriteSheet()
        sprite_player = sprite_player.get_image(player_idle, 2000, 1890, 0.4)
        fofo = char.MainPlayer(player_start_x, player_start_y, sprite_player, self.width, self.height, platform_group, GRAVITY)        

        #loop principal do jogo
        while game_on:
            clock.tick(60) 

            
            if fofo.rect.bottom > SCREEN_HEIGHT:
                fofo.kill(death_fx)
                game_on = False

            else:
                fofo.move(group_de_inimigos, expresso_group)

            # Gerando Cenário
            BKGD = bg_gen.ScrollBackground(self.height, screen, scroll, 5, bkgd)
            scroll = BKGD.scroll_bkgd()

            for plataforma in platform_group:
                plataforma.rect.y += 0.5

            current_time = py.time.get_ticks()
            if current_time - last_update >= 2500:
                platform_group = generate_new_platform(platform_group, self.width, self.height, imagem_plataforma)
                last_update = current_time

            plat.draw(screen, platform_group)

            #Criando inimigos
            if len(group_de_inimigos) == 0:
                enemy_x = random.randint(80, SCREEN_WIDTH - 80)
                enemy_y = random.randint(80, SCREEN_HEIGHT - 80)
                inimigo = char.Professor(enemy_x, enemy_y, sprite_enemy, SCREEN_WIDTH, SCREEN_HEIGHT)
                group_de_inimigos.add(inimigo)

            group_de_inimigos.update()
                 
            #Atualizando inimigos
            for inimigo in group_de_inimigos:
                inimigo.rect.y += 0.5

            #Criando copinhos
            if len(expresso_group) == 0:
                expresso_x = random.randint(100, SCREEN_WIDTH - 100)
                expresso_y = random.randint(100, SCREEN_HEIGHT - 100)
                expresso = item.Item(expresso_x, expresso_y, imagem_expresso, SCREEN_WIDTH, SCREEN_HEIGHT)
                expresso_group.add(expresso)

            expresso_group.update()
                 
            #Atualizando copinhos
            for expresso in expresso_group:
                expresso.rect.y += 0.5

            #Desenhando o jogador
            expresso_group.draw(screen)
            group_de_inimigos.draw(screen)
            fofo.draw(screen)

            for event in py.event.get():
                if event.type == py.QUIT:
                    game_on = False
            
            #YOU WON
            if current_time >= 24000:
                menu.you_won(screen, menu_image, you_won_image, FPS, self.width, self.height, WHITE, BLUE)
                

            py.display.update()
