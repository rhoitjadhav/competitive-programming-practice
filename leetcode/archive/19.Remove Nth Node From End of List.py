# Remove Nth Node From End of List
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, l: ListNode, n: int) -> ListNode:
        count = 0
        h = l
        while l:
            count += 1
            l = l.next
        
        key = count - n + 1
        count = 1
        new = ListNode(0, h)
        last = new
        while h:
            if key == count:
                last.next = h.next
                break

            count += 1
            last = h
            h = h.next

        return new.next
    
    def view(self, l):
        while l:
            print(l.val, end=" ")
            l = l.next

s = Solution()

a = ListNode(1)
b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)

a.next = b
# b.next = c
# c.next = d
# d.next = e

n = 2
out = s.removeNthFromEnd(a, n)
s.view(out)
