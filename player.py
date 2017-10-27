import pygame
from point import *

class Player:
	def __init__(self, pos, speed, size):
		self.pos = pos
		self.speed = speed
		self.size = size
		self.color = (255,0,0)
		self.length = 5
		self.coords = [pos]
		self.direction = 0

	def update(self):
		print("")

	def render(self, screen):
		for coord in self.coords:
			pygame.draw.ellipse(screen, self.color, (coord.x, coord.y, self.size, self.size), 1)