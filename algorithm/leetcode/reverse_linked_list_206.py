from operator import ne
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

# [풀이1. 재귀 구조로 뒤집기]==========================================================

class Solution1:
    def reverseList(self, head: Optional[ListNode]):  # -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)

# [풀이2. 반복 구조로 뒤집기]==========================================================

class Solution2:
    def reverseList(self, head: Optional[ListNode]):  # -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
