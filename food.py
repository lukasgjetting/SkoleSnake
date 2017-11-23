import random, pygame, utils
from point import *

class Food:
	def __init__(self, maxX, maxY):
		self.pos = Point(int(random.random()*(maxX*0.8)+(maxX*0.1)), int(random.random()*maxY))
		self.size = 15
		self.color = (0, 0, 255)

	def render(self, screen):
		pygame.draw.ellipse(screen, self.color, (self.pos.x-(self.size/2), self.pos.y-(self.size/2), self.size, self.size), 1)

	def collidesWithPlayer(self, player):
		if(
			utils.equalsWithMargin(self.pos.x, player.pos.x, self.size/2+player.size/4) and
			utils.equalsWithMargin(self.pos.y, player.pos.y, self.size/2+player.size/4)
		):
			return True
		else:
			return False