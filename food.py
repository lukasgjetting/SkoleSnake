import random, pygame
from point import *

class Food:
	def __init__(self, maxX, maxY):
		self.pos = Point(int(random.random()*maxX), int(random.random()*maxY))
		self.size = 15
		self.color = (0, 0, 255)

	def render(self, screen):
		pygame.draw.ellipse(screen, self.color, (self.pos.x, self.pos.y, self.size, self.size), 1)

	def collidesWithPlayer(self, player):
		if(
			player.pos.x > self.pos.x - player.size and
			player.pos.y > self.pos.y - player.size and
			player.pos.x < self.pos.x + self.size and
			player.pos.y < self.pos.y + self.size
		):
			return True