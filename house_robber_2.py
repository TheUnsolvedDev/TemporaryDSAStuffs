class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [-1 for i in range(len(nums)+1)]
        dp2 = [-1 for i in range(len(nums)+1)]
        def recurse(ind,array,dp):
            if ind == 0:
                return array[ind]
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            else:
                left = array[ind] + recurse(ind-2,array,dp)
                right = recurse(ind-1,array,dp)
                dp[ind] = max(left,right)
                return dp[ind]
        return max(recurse(len(nums)-2,nums[:-1],dp1),recurse(len(nums)-2,nums[1:],dp2))