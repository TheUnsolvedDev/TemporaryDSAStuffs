def reverse_array(array, start, end):
	if start < end:
		array[start],array[end] = array[end],array[start]
		reverse_array(array, start + 1, end - 1)
	return array

if __name__ == '__main__':
	array = [1, 2, 3, 4, 5, 6, 7]
	print(reverse_array(array, 0, len(array) - 1))