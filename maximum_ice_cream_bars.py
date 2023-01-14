class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        for i in sorted(costs):
            if i <= coins:
                count+=1
                coins-=i
        return count