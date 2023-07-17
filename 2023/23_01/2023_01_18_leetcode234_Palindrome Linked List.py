# https://leetcode.com/problems/palindrome-linked-list/submissions/880327173/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = deque()
        cur_head = head
        while cur_head is not None:
            temp.append(cur_head.val)
            cur_head = cur_head.next
        while len(temp) > 1:
            if temp.popleft() != temp.pop():
                return False
        return True