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


class Bat:
    """
    Organização Principal do Jogo
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
        py.mixer.music.set_volume(0.7)
        py.mixer.music.play(-1)
        jump_fx = py.mixer.Sound("assets\\jumpland44100.mp3")
        death_fx = py.mixer.Sound("assets\\deathsound.mp3")

        #Carregando imagens necessárias
        player_idle = py.image.load("assets\calunio.png").convert_alpha()
        enemy_idle = py.image.load(r"assets\vilao.png").convert_alpha()
        imagem_plataforma = py.image.load("assets\plataforma.png")
        bkgd = py.image.load("assets\imagem_final.jpg").convert()
        
        #Geração de Plataformas
        platform_group = py.sprite.Group()
        group_de_inimigos = py.sprite.Group()

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

        #Criando inimigo
        sprite_enemy = sprites.SpriteSheet()
        sprite_enemy = sprite_enemy.get_image(enemy_idle, 1600, 1600, 0.09)

        #loop principal do jogo
        while game_on:
            clock.tick(60) 

            
            if fofo.rect.bottom > SCREEN_HEIGHT:
                fofo.kill(death_fx)
                game_on = False

            else:
                fofo.move()

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
            
            #Atualizando inimigos
            for inimigo in group_de_inimigos:
                inimigo.rect.y += 0.5

            #Desenhando inimigos periodicamente
            if current_time - last_update >= 1000:
                altura_do_inimigo = 144
                enemy_image = sprite_enemy
                p = random.randint(0, len(platform_group) - 1)
                for plataforma in platform_group:
                    if p == 0:
                        break
                    p == 0
                    # Ajuste as coordenadas y para posicionar os inimigos sobre as plataformas
                    enemy_x = plataforma.rect.centerx  # Define a coordenada x igual ao centro da plataforma
                    enemy_y = plataforma.rect.top - altura_do_inimigo  # Define a coordenada y acima da plataforma
                    
                    # Crie o inimigo usando as coordenadas definidas
                    novo_inimigo = char.Professor(enemy_x, enemy_y, enemy_image)
                    group_de_inimigos.add(novo_inimigo)

                last_update = current_time

            char.draw(screen, group_de_inimigos)

            #Desenhando o jogador
            fofo.draw(screen)

            for event in py.event.get():
                if event.type == py.QUIT:
                    game_on = False

            py.display.update()
