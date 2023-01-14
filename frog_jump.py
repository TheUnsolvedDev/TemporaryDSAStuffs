from os import *
from sys import *
from collections import *
from math import *

from typing import *

def recurse(ind,heights,dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]
    else:
        left = recurse(ind-1,heights,dp) + abs(heights[ind] - heights[ind-1])
        right = 10**9
        if ind > 1:
            right = recurse(ind-2,heights,dp) + abs(heights[ind] - heights[ind-2])
        dp[ind] = min(left,right)
        return dp[ind] 
    
def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    dp = [-1 for i in range(n+1)]
    sol = recurse(n-1,heights,dp)
    return sol

if __name__ == "__main__":
    print(frogJump(3,[10,20,30,10]))