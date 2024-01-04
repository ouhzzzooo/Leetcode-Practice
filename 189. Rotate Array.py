class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n == 0:
            return []
        if k == 0:
            return nums

        if k > n:
            k = k % n
        first = nums[n-k: n]
        for i in range(k):
            nums.pop()
        for i in range(1, len(first) + 1):
            nums.insert(0, first[-i])
