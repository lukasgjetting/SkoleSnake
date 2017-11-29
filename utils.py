import random, constants
from food import *

def equalsWithMargin(a, b, margin):
	if(a-margin <= b and a+margin >= b):
		return True
	return False 


# Difficulty should be 0-10
def generateFoods(word, difficulty):
	foods = []

	for letter in word:
		foods.append(Food(letter))

	for i in range(difficulty*constants.DIFFICULTY_MODIFIER):
		foods.append(Food(constants.LETTERS[int(random.randint(0, len(constants.LETTERS)-1))]))

	return foods