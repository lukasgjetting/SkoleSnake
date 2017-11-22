import sys, pygame
from player import *
from point import *
from food import *

GAME_WIDTH = 480
GAME_HEIGHT = 480

pygame.init()

clock = pygame.time.Clock()

size = width, height = GAME_WIDTH, GAME_HEIGHT

screen = pygame.display.set_mode(size)

player = Player(Point(GAME_WIDTH/2,GAME_HEIGHT/2), 1, 10)
food = Food(GAME_WIDTH, GAME_HEIGHT)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.turn("l")
	if keys[pygame.K_RIGHT]:
		player.turn("r")

	screen.fill((255,255,255))

	if(food.collidesWithPlayer(player)):
		player.length += 1
		food = Food(GAME_WIDTH, GAME_HEIGHT)

	player.update()

	player.render(screen)
	food.render(screen)

	pygame.display.flip()

	
	clock.tick(15)