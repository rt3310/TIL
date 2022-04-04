from platform import node
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]): # -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            node = list1
            list1 = list1.next
        else:
            node = list2
            list2 = list2.next
        
        node_head = node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            elif list2.val <= list1.val:
                node.next = list2
                node = node.next
                list2 = list2.next
        
        if list1 is not None:
            node.next = list1
        elif list2 is not None:
            node.next = list2

        return node_head
            
a = ListNode()
b = ListNode()

a.val = 1
a.next = ListNode()
a.next.val = 2
a.next.next = ListNode()
a.next.next.val = 4

b.val = 1
b.next = ListNode()
b.next.val = 3
b.next.next = ListNode()
b.next.next.val = 4

Solution().mergeTwoLists(a, b)

# [풀이1. 재귀 구조로 연결]==========================================================

class Solution1:
    # -> Optional[ListNode]:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

a = ListNode()
b = ListNode()

a.val = 1
a.next = ListNode()
a.next.val = 2
a.next.next = ListNode()
a.next.next.val = 4

b.val = 1
b.next = ListNode()
b.next.val = 3
b.next.next = ListNode()
b.next.next.val = 4

Solution1().mergeTwoLists(a, b)
