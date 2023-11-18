class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        #Sorted and find Middle which is majority element

        nums = sorted(nums)
        
        mid = len(nums) // 2

        return nums[mid]


        # Dict Method

        # num_dict = {}

        # for i in nums:
        #     if i in num_dict :
        #         num_dict[i] += 1
        #     else:
        #         num_dict[i] = 1
        # print(num_dict)

        # max_value = max(num_dict.values())
        # max_key = [k for k , v in num_dict.items() if v == max_value]
        # res = max_key[0]
        # print(res)
        # return res
