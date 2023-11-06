class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #binary search
        #find only half of it to make complexity O(log n)
        #Space complexity : O(1)
        #Time complexity : O(log n)
        
        l = 0
        r = len(nums) - 1
    
        while r >= l:
            mid = (l + r) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        return l 
