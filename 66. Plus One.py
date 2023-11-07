class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        total = 0
        k = 1

        for i in range(1, len(digits) + 1):
            total += digits[-i] * k
            k *= 10
        total += 1

        res = [int(x) for x in str(total)]
        return res
