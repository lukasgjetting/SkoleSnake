import pygame, math, constants
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
		self.turnSpeed = 15
		self.hp = 3
		self.heartImage = pygame.image.load("heart.png")

	def update(self):
		# Tilføj et nyt punkt til slangen
		if(self.length >= len(self.coords)):
			self.coords.insert(0, self.calculateNewPos())
		if(self.length <= len(self.coords)):
			self.coords.pop()

	def calculateNewPos(self):
		newPos= Point(self.pos.x+self.size*math.cos(math.radians(self.direction)), self.pos.y+self.size*math.sin(math.radians(self.direction)))
		
		# Wrap x-axis
		if(newPos.x > constants.GAME_WIDTH):
			newPos.x -= constants.GAME_WIDTH;
		elif(newPos.x < 0):
			newPos.x += constants.GAME_WIDTH

		# Wrap y-axis
		if(newPos.y > constants.GAME_HEIGHT):
			newPos.y -= constants.GAME_WIDTH
		elif(newPos.y < 0):
			newPos.y += constants.GAME_HEIGHT

#		for i in range(self.length-1):
#			print(self.coords[i])

		self.pos = newPos
		return self.pos

	def render(self, screen):
		for coord in self.coords:
			pygame.draw.ellipse(screen, self.color, (coord.x-(self.size/2), coord.y-(self.size/2), self.size, self.size), 1)
		
		x = 20
		for i in range(self.hp):
			screen.blit(self.heartImage, (x, constants.GAME_HEIGHT-20, 32, 32))
			x = x + 52

	def turn(self, direction):
		if(direction == "l"):
			self.direction -= self.turnSpeed
		elif(direction == "r"):
			self.direction += self.turnSpeed