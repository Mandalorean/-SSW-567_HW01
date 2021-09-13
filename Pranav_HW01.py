

def checkTriangle(x,y,z):
	if x + y > z and x + z > y and y + z > x and (x!=0 and y!=0 and z!=0):
		if x == y == z :
			return "Equilateral triangle"
		else:
			if z * z == (y * y) + (x * x) or x * x == (y * y) + (z * z) or y * y == (z * z) + (x * x):
				if x == y or y == z or z == x:
					return "Isosceles right triangle"
				else:
					return "Scalene right triangle"
			else:
				if x == y or y == z or z == x:
					return "Isosceles triangle"
				else:
					return "Scalene triangle"
	else:
		return "Invalid triangle"


if __name__ == '__main__':
    # examples of running the code
    print('{}'.format(checkTriangle(4,4,5)))