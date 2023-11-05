class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        data = { ")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in data:
                temp = stack.pop() if stack else "#"
                if temp != data[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0 :
            return False
        return True
