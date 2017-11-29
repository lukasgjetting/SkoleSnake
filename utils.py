import random, constants
from food import *

def equalsWithMargin(a, b, margin):
	if(a-margin <= b and a+margin >= b):
		return True
	return False 


# Difficulty should be 0-10
def generateFoods(word, noSpawnLocation, difficulty):
	foods = []

	for letter in word:
		newFood = Food(letter)
		while(equalsWithMargin(newFood.pos.x, noSpawnLocation.x, constants.FOOD_NO_SPAWN_RADIUS) or equalsWithMargin(newFood.pos.y, noSpawnLocation.y, constants.FOOD_NO_SPAWN_RADIUS)):
			newFood = Food(letter)
		foods.append(newFood)

	for i in range(difficulty*constants.DIFFICULTY_MODIFIER):
		newFood = Food(constants.LETTERS[int(random.randint(0, len(constants.LETTERS)-1))])
		while(equalsWithMargin(newFood.pos.x, noSpawnLocation.x, constants.FOOD_NO_SPAWN_RADIUS) or equalsWithMargin(newFood.pos.y, noSpawnLocation.y, constants.FOOD_NO_SPAWN_RADIUS)):
			newFood = Food(letter)
		foods.append(newFood)

	return foods