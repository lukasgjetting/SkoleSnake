import sys, pygame, constants, utils, time
from player import *
from point import *
from food import *

pygame.init()

letterFont = pygame.font.SysFont("monospace", 15)

clock = pygame.time.Clock()

size = width, height = constants.GAME_WIDTH, constants.GAME_HEIGHT

screen = pygame.display.set_mode(size)

player = Player(Point(constants.GAME_WIDTH/2,constants.GAME_HEIGHT/2), 1, 10)

word = "APPLE"
letterIndex = 0

foods = utils.generateFoods(word, 1)

pause = True

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

	# Update player
	player.update()

	for food in foods:
		# Check for food collision with player
		if(food.collidesWithPlayer(player)):
			player.length += 1
			foods.remove(food)


	player.render(screen)

	# Render food
	for food in foods: 
		food.render(screen, letterFont)

	pygame.display.flip()

	if(pause):
		time.sleep(3)
		pause = False
	
	clock.tick(15)