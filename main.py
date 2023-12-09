import sys
sys.path.insert(0, "./gameplay")

from BAT import bat

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

jogo = Bat(SCREEN_HEIGHT, SCREEN_WIDTH)

jogo.start()