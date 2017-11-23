def equalsWithMargin(a, b, margin):
	if(a-margin <= b and a+margin >= b):
		return True
	return False 