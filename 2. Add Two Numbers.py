# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        stack2 = []

        while l1 != None:
            stack1.insert(0, l1.val)
            l1 = l1.next
        while l2 != None:
            stack2.insert(0, l2.val)
            l2 = l2.next
        val1 = ''.join(map(str, stack1))
        val2 = ''.join(map(str, stack2))
        res = int(val1) + int(val2)
        
        res_str = str(res)

        head = ListNode()

        current = head
        for digit_str in reversed(res_str):
            digit = int(digit_str)
            current.next = ListNode(digit)
            current = current.next
        
        return head.next
