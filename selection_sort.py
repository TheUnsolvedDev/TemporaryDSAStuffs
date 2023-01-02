def selection_sort(array):
	for i in range(len(array)-1):
		for j in range(i+1,len(array)):
			if array[i] > array[j]:
				array[i],array[j] = array[j],array[i]
	return array

if __name__ == '__main__':
	array = [i for i in range(10,-1,-1)]
	print(selection_sort(array))