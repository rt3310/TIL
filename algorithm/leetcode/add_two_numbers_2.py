from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]): # -> Optional[ListNode]:
        nums = []
        node = ListNode()
        answer = node
        
        upper = 0
        while l1 is not None or l2 is not None and upper != 0:
            if l1 is None:
                num1 = 0
            else:
                num1 = l1.val
            if l2 is None:
                num2 = 0
            else:
                num2 = l2.val
            
            num = num1 + num2 + upper
            nums.append(num % 10)
            upper = num // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        for i, v in enumerate(nums):
            print(v, end=' ')
            node.val = v
            if i != len(nums):
                node.next = ListNode()
                node = node.next
        
        return answer

a = ListNode()
a_head = a
b = ListNode()
b_head = b

a_list = [9,9,9,9,9,9,9]
for i in a_list:
    a.val = i
    a.next = ListNode()
    a = a.next

b_list = [9,9,9,9]
for j in b_list:
    b.val = i
    b.next = ListNode()
    b = b.next

print(Solution().addTwoNumbers(a_head, b_head))

# [풀이1. 자료형 변환]==========================================================

class Solution1:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode): # -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode): # -> ListNode:
        list: List = []
        
        while node:
            list.append(node.val)
            node = node.next
        
        return list
    
    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: ListNode): # -> ListNode:
        prev: ListNode = None
        
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]): # -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        
        # 최종 결과 계산 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))
    
# [풀이2. 전가산기 구현]==========================================================

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]): # -> Optional[ListNode]:
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next