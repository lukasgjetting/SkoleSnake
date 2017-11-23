import sys, pygame, constants
from player import *
from point import *
from food import *

pygame.init()

clock = pygame.time.Clock()

size = width, height = constants.GAME_WIDTH, constants.GAME_HEIGHT

screen = pygame.display.set_mode(size)

player = Player(Point(constants.GAME_WIDTH/2,constants.GAME_HEIGHT/2), 1, 10)
food = Food(constants.GAME_WIDTH, constants.GAME_HEIGHT)
	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		player.turn("l")
	if keys[pygame.K_RIGHT]:
		player.turn("r")


	# Update food
	if(food.collidesWithPlayer(player)):
		player.length += 1
		food = Food(constants.GAME_WIDTH, constants.GAME_HEIGHT)
		#while True:
		#	print("xd")

	# Update player
	player.update()

	screen.fill((255,255,255))

	player.render(screen)
	food.render(screen)

	pygame.display.flip()

	
	clock.tick(15)