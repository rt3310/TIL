from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]):# -> Optional[ListNode]:
        if not head:
            return None
        
        answer = head
        odd = head
        even = head.next
        even_nodes = even
        
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_nodes
        
        while answer:
            print(answer.val)
            answer = answer.next
        return answer
    
a = ListNode()
a_head = a

a_list = [1]
for i in a_list:
    a.val = i
    a.next = ListNode()
    a = a.next

Solution().oddEvenList(a_head)

# [풀이1. 반복 구조로 홀짝 노드 처리]===================================================

class Solution1:
    def oddEvenList(self, head: Optional[ListNode]):# -> Optional[ListNode]:
        # 예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 해결
        odd.next = even_head
        return head