def next_permutation(nums):
    ind1 = 0
    ind2 = 0
    if nums == None or len(nums) <= 1:
    	return 

    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            ind1 = i
            break

    for i in range(len(nums)-1, ind1, -1):
        if nums[i] > nums[ind1]:
            ind2 = i 
            break

    nums[ind1], nums[ind2] = nums[ind2], nums[ind1]

    for i in range(ind1+1, len(nums)-1):
        nums[i], nums[len(nums)-i+ind1] = nums[len(nums)-i+ind1], nums[i]
    return nums


if __name__ == '__main__':
    print(next_permutation([3,2,1]))
