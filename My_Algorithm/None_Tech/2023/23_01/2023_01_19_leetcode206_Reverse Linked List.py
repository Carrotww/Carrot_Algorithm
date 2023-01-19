# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# 재귀
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev=None):
            if not node:
                return prev
            next = node.next
            node.next = prev
            return reverse(next, node)
        return reverse(head)

# 반복구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        
        while node:
            next = node.next
            node.next = prev
            
            prev = node
            node = next
        
        return prev