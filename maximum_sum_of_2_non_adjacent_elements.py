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
    
    
    
if __name__ == '__main__':
    array = [5, 5, 10, 100, 10, 5]
    dp = [-1 for i in range(len(array)+1)]
    
    print(recurse(len(array)-1,array,dp))