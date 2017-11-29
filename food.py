import random, pygame, utils, constants
from point import *

class Food:
	def __init__(self, letter):
		self.pos = Point(int(random.random()*(constants.GAME_WIDTH*0.8)+(constants.GAME_WIDTH*0.1)), int(random.random()*(constants.GAME_HEIGHT*0.8)+(constants.GAME_HEIGHT*0.1)))
		self.letter = letter
		self.size = 25
		self.color = (0, 0, 255)

	def render(self, screen, font):
		pygame.draw.ellipse(screen, self.color, (self.pos.x-(self.size/2), self.pos.y-(self.size/2), self.size, self.size), 1)
	
		# Draw letter
		renderedLetter = font.render(self.letter, 1, (0, 0, 0))

		text_width = renderedLetter.get_width()
		text_height = renderedLetter.get_height()

		screen.blit(renderedLetter, (self.pos.x-text_width/2, self.pos.y-text_height/2))

	def collidesWithPlayer(self, player):
		if(
			utils.equalsWithMargin(self.pos.x, player.pos.x, self.size/2+player.size/4) and
			utils.equalsWithMargin(self.pos.y, player.pos.y, self.size/2+player.size/4)
		):
			return True
		else:
			return False