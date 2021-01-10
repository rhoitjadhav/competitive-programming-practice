# Reverse Linked List
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None
        l = head.next
        output = ListNode(head.val)

        while l:
            output = ListNode(l.val, output)
            l = l.next

        return output

    def reverse(self, head: ListNode) -> ListNode:
        output = ListNode(head.val)
        def recursive(l):
            global output
            if l:
                output = ListNode(l.val)
                recursive(l.next)
            return output

        return recursive(head.next) 
            

    def view(self, l):
        while l:
            print(l.val)
            l = l.next

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

output = s.reverse(a)
s.view(output)
