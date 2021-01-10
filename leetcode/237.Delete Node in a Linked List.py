# Delete Node in a Linked List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pass

    def view(self, l):
        while l:
            print(l.val)
            l = l.next

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(6)
d = ListNode(3)
e = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = e

s.deleteNode(a)
