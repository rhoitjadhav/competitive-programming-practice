from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = head
        j = head

        while i or j:
            if i is None or j is None or i.next is None or j.next is None:
                return False
            i = i.next
            j = j.next.next

            if i == j:
                return True

        return False
