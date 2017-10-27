import pygame, math
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
		# Tilføj et nyt punkt til slangen
		self.coords.insert(0, self.calculateNewPos())
		print(len(self.coords))
		if(self.length <= len(self.coords)):
			self.coords.pop()

	def calculateNewPos(self):
		newPos= Point(self.pos.x+self.size*math.cos(math.radians(self.direction)), self.pos.y+self.size*math.sin(math.radians(self.direction)))
		self.pos = newPos
		return self.pos

	def render(self, screen):
		for coord in self.coords:
			pygame.draw.ellipse(screen, self.color, (coord.x, coord.y, self.size, self.size), 1)