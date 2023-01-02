def max_subarray(nums):
	sums = 0
	maxm = nums[0]
	for i in nums:
		sums += i
		maxm = max(maxm,sums)
		if sums <= 0:
			sums = 0
	return maxm

if __name__ == "__main__":
	print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))