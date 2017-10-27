import sys, pygame
from player import *
from point import *

pygame.init()

clock = pygame.time.Clock()

size = width, height = 480, 480

screen = pygame.display.set_mode(size)

player = Player(Point(240,240), 2, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	sys.exit()

    screen.fill((0,0,0))
    player.render(screen)
    player.update()
    pygame.display.flip()
    clock.tick(15)