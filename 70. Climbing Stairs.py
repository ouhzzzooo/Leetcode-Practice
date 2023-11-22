class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = 0
        second = 1
        for i in range(n - 1):
            third = second + first
            first = second 
            second = third
        return first + second
