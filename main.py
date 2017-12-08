import sys, pygame, random, constants, utils, time
from player import *
from point import *
from food import *

pygame.init()

letterFont = pygame.font.SysFont("monospace", 15)
wordFont = pygame.font.SysFont("monospace", 32)

clock = pygame.time.Clock()

size = width, height = constants.GAME_WIDTH, constants.GAME_HEIGHT

screen = pygame.display.set_mode(size)

player = Player(Point(constants.GAME_WIDTH/2,constants.GAME_HEIGHT/2), 1, 10)

word = ""
letterIndex = 0
letters = ""
foods = None
image = None

pause = True

while 1:
	if(word == ""):
		word = constants.WORDS[random.randint(0, len(constants.WORDS)-1)]
		letterIndex = 0
		letters = ""
		foods = utils.generateFoods(word, player.pos, 1)
		image = pygame.image.load("images/" + word + ".png")

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
			foods.remove(food)

			if(food.letter == word[letterIndex]):
				letters += food.letter
				letterIndex += 1
				player.length += 1

				if(letterIndex == len(word)):
					word = ""
			else:
				player.length -= 1
				foods.append(Food(food.letter))


	screen.blit(image, image.get_rect())
	
	player.render(screen)

	# Render food
	for food in foods: 
		food.render(screen, letterFont)

	renderedWord = wordFont.render(letters, 1, (0,0,0))
	screen.blit(renderedWord, (constants.GAME_WIDTH/2, constants.GAME_HEIGHT-100))

	pygame.display.flip()

	if(pause):
		time.sleep(3)
		pause = False
	
	clock.tick(15)