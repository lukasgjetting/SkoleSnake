import sys, pygame
from player import *
from point import *

pygame.init()

size = width, height = 480, 480

screen = pygame.display.set_mode(size)

player = Player(Point(240,240), 2, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()

    player.render(screen)

    pygame.display.flip()