import numpy as np

def make_zero(array):
	find_zero = []
	for i in range(len(array)):
		for j in range(len(array[0])):
			if array[i][j] == 0:
				find_zero.append((i,j))
	
	for (i,j) in find_zero:
		for rows in range(len(array[0])):
			array[i][rows] = 0

		for columns in range(len(array)):
			array[columns][j] = 0
	
	return array

if __name__ == "__main__":
	make_zero([[0,1,2,0],[3,4,5,2],[1,3,1,5]])