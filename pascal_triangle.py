def generate(numRows):
	lists = []
	for i in range(numRows):
		temp = [1 for i in range(i + 1)]
		temp[0] = temp[-1] = 1
		for j in range(1,i):
			temp[j] = lists[i-1][j-1] + lists[i-1][j]
		lists.append(temp)
	print(lists)

if __name__ == '__main__':
	generate(6)
