import pygame as py
import sys

def draw_text(screen, font, text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu(screen, menu_image, title_image, FPS, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLUE):
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

