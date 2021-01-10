# Remove Linked List Elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        last = ListNode(-1, head)
        l = head
        output = last
        while l:
            if l.val == val:
                last.next = l.next
            else:
                last = last.next
            l = l.next
        
        return output.next

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
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


output = s.test(a)
print(output)
# s.view(output)


