def sum_n(number):
	if number == 1:
		return 1
	else:
		return number + sum_n(number - 1)

if __name__ == '__main__':
	print(sum_n(100))