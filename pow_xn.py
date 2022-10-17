class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = abs(n)
        ans = 1

        while num > 0:
            if num % 2:
                ans *= x
                num -= 1
            else:
                x = x*x
                num //= 2
        if n > 0:
            return ans
        else:
            return 1/ans
