import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        stack = []
        stack1 = []
        value = str(x)
        for i in value :
            stack.append(i)
        for j in range (1, len(stack) + 1) :
            stack1.append(stack[-j])
        for k in range (0, len(stack)):
            if stack[k] != stack1[k]:
                return False
        return True
