"""
Criação das telas do jogo
"""

import pygame as py
import sys

def draw_text(screen, font, text, color, x, y):
    """
    Desenha um texto na tela.

    Parameters:
        screen (Surface): A superfície onde o texto será desenhado.
        font (Font): O objeto de fonte do pygame.
        text (str): O texto a ser desenhado.
        color (tuple): A cor do texto no formato RGB.
        x (int): A coordenada x do centro do texto.
        y (int): A coordenada y do centro do texto.
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu(screen, menu_image, title_image, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE):
    """
    Função para exibir o menu principal do jogo.

    Parameters:
        screen (Surface): A superfície onde o menu será exibido.
        menu_image (Surface): A imagem de fundo do menu.
        title_image (Surface): A imagem do título do jogo.
        FPS (int): A taxa de quadros por segundo.
        SCREEN_WIDTH (int): A largura da tela do jogo.
        SCREEN_HEIGHT (int): A altura da tela do jogo.
        WHITE (tuple): A cor branca no formato RGB.
        BLUE (tuple): A cor azul no formato RGB.
    """
    font = py.font.Font(None, 36)
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    return
                elif quit_rect.collidepoint(event.pos):
                    py.quit()
                    sys.exit()

        screen.blit(menu_image, (0, 0))

        title_rect = title_image.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_image, title_rect)

        new_game_rect = py.draw.rect(screen, BLUE, (200, 200, 300, 50))
        quit_rect = py.draw.rect(screen, BLUE, (200, 300, 300, 50))

        draw_text(screen, font, "New Game", WHITE, SCREEN_WIDTH // 2, 225)
        draw_text(screen, font, "Quit", WHITE, SCREEN_WIDTH // 2, 325)

        py.display.flip()

        py.time.Clock().tick(FPS)

def game_over(screen, game_over_img, title_image, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE):
    """
    Função para exibir a tela de Game Over do jogo.

    Parameters:
        screen (Surface): A superfície onde a tela de Game Over será exibida.
        game_over_img (Surface): A imagem de fundo da tela de Game Over.
        title_image (Surface): A imagem do título do jogo.
        FPS (int): A taxa de quadros por segundo.
        SCREEN_WIDTH (int): A largura da tela do jogo.
        SCREEN_HEIGHT (int): A altura da tela do jogo.
        WHITE (tuple): A cor branca no formato RGB.
        BLUE (tuple): A cor azul no formato RGB.
    """
    font = py.font.Font(None, 36)
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    pass
                elif quit_rect.collidepoint(event.pos):
                    py.quit()
                    sys.exit()

        screen.blit(game_over_img, (0, 0))

        title_rect = title_image.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_image, title_rect)

        new_game_rect = py.draw.rect(screen, BLUE, (200, 200, 300, 50))
        quit_rect = py.draw.rect(screen, BLUE, (200, 300, 300, 50))

        draw_text(screen, font, "Restart Game", WHITE, SCREEN_WIDTH // 2, 225)
        draw_text(screen, font, "Quit", WHITE, SCREEN_WIDTH // 2, 325)

        py.display.flip()

        py.time.Clock().tick(FPS)

def you_won(screen, you_won_img, title_image, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE):
    """
    Função para exibir a tela de vitória do jogo.

    Parameters:
        screen (Surface): A superfície onde a tela de vitória será exibida.
        you_won_img (Surface): A imagem de fundo da tela de vitória.
        title_image (Surface): A imagem do título do jogo.
        FPS (int): A taxa de quadros por segundo.
        SCREEN_WIDTH (int): A largura da tela do jogo.
        SCREEN_HEIGHT (int): A altura da tela do jogo.
        WHITE (tuple): A cor branca no formato RGB.
        BLUE (tuple): A cor azul no formato RGB.
    """
    font = py.font.Font(None, 36)
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    pass
                elif quit_rect.collidepoint(event.pos):
                    py.quit()
                    sys.exit()

        screen.blit(you_won_img, (0, 0))

        title_rect = title_image.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title_image, title_rect)

        new_game_rect = py.draw.rect(screen, BLUE, (200, 200, 300, 50))
        quit_rect = py.draw.rect(screen, BLUE, (200, 300, 300, 50))

        draw_text(screen, font, "Restart Game", WHITE, SCREEN_WIDTH // 2, 225)
        draw_text(screen, font, "Quit", WHITE, SCREEN_WIDTH // 2, 325)

        py.display.flip()

        py.time.Clock().tick(FPS)

