def sort(nums):
	left = 0
	right = len(nums)-1
	index = 0
	while index <= right:
		if nums[index] == 0:
			nums[left], nums[index] = nums[index], nums[left]
			left += 1
		if nums[index] == 2:
			nums[right],nums[index] = nums[index],nums[right]
			right -= 1
			index -= 1
		index += 1
		print(nums)


if __name__ == '__main__':
	sort([2,0,2,1,1,0,0,1,2,2,1,2,0,0,1])
