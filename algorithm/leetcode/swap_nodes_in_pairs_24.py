from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]): # -> Optional[ListNode]:
        node = head
        
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        
        return node
    
# [풀이1. 값만 교환]===================================================

class Solution1:
    def swapPairs(self, head: Optional[ListNode]): # -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        
        return head

# [풀이2. 반복 구조로 스왑]===================================================

class Solution2:
    def swapPairs(self, head: Optional[ListNode]): # -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            # prev가 b를 가리키도록 할당
            prev.next = b
            
            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next 
        
        return root.next
    
# [풀이3. 재귀 구조로 스왑]===================================================

class Solution3:
    def swapPairs(self, head: Optional[ListNode]): # -> O0ptional[ListNode]:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head