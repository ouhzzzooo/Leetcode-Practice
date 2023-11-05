class Solution:
    def romanToInt(self, s: str) -> int:
        
        data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0

        for i in range(len(s) - 1):
            if data[s[i]] < data[s[i+1]]:
                value -= data[s[i]]
            else:
                value += data[s[i]]
        return value + data[s[-1]]
