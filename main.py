import sys, pygame
from player import *
from point import *

pygame.init()

clock = pygame.time.Clock()

size = width, height = 480, 480

screen = pygame.display.set_mode(size)

player = Player(Point(240,240), 1, 10)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.turn("l")
	if keys[pygame.K_RIGHT]:
		player.turn("r")

	screen.fill((0,0,0))
	player.render(screen)
	player.update()
	pygame.display.flip()
	clock.tick(15)