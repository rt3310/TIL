from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]): # -> Optional[ListNode]:
        new_head = None
        
        while head:
            node = head
            head = head.next
            node.next = new_head
            new_head = node
        
        while new_head:
            print(new_head.val)
        
        return new_head


a = ListNode()

a.val = 1
a.next = ListNode()
a.next.val = 2
a.next.next = ListNode()
a.next.next.val = 3
a.next.next.next = ListNode()
a.next.next.next.val = 4
a.next.next.next.next = ListNode()
a.next.next.next.next.val = 5

Solution().reverseList(a)
