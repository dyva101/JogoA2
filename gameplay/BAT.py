import pygame as py
import character as char

class Bat():
    """
    Organização Principal do Jogo
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def start(self):
        pygame.init()

        #Variáveis
        current_time = pygame.time.get_ticks()
        last_update = pygame.time.get_ticks()
        clock = pygame.time.Clock() # FPS
        animation_cooldonw = 500
        isjumping = False
        time_counting = 0
        game_on = True
        scroll = 0
        GRAVITY = 0.03
        action = 0
        frame = 0

        # Criando uma tela
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("BAT: Uma Perigosa Jornada Universitária")

        #Criando player
        fofo = char.Main_player(player_start_x, player_start_y , idle_1, SCREEN_WIDTH, SCREEN_HEIGHT, platform_group, GRAVITY)

        #Carregando imagens necessárias
        player_idle = pygame.image.load("imgs and songs/calunio.png").convert_alpha()
        sprite_sheet = sp.SpriteSheet(player_idle)
        imagem_plataforma = pygame.image.load("imgs and songs/2dplatform.png")
        bkgd = pygame.image.load("imgs and songs/total_bkgd.png").convert()     

        #loop principal do jogo
        while game_on:
            clock.tick(60) 
            
            fofo.move()

            # Gerando fundo e plataformas
            new_scroll = bg_gen.scroll_bkgd(SCREEN_HEIGHT, screen, scroll, bkgd)
            scroll = new_scroll
            plat.draw(screen, platform_group)
            
            # Desenhando o jogador
            fofo.draw(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_on = False

            pygame.display.update()
    
    def finish():
        pass