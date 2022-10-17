def bubble_sort(array):
	for i in range(len(array)):
		for j in range(0, len(array)-i-1):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
			print(array)
	return array

if __name__ == '__main__':
	array = [i for i in range(10,-1,-1)]
	print(bubble_sort(array))