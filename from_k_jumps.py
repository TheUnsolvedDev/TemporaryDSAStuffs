def recurse(ind,k,heights,dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    else:
        right = 10**9
        for i in range(1,k+1):
            if (ind - i)>= 0:
                jump = recurse(ind-i,k,heights,dp) + abs(heights[ind] - heights[ind-i])
            dp[ind] = min(jump,right)
        return dp[ind] 
    
def jump(n,k,array):
    dp = [-1 for i in range(n)]
    sol = recurse(n-1,k,array,dp)
    return sol

if __name__ == "__main__":
    n,k = list(map(int,input().split(" ")))
    array = list(map(int,input().split(" ")))
    
    print(jump(n,k,array))