# Remove Duplicates from Sorted List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        
        ptr, last = head.next, head
        
        while ptr:
            if ptr.val == last.val:
                last.next = ptr.next
            else:
                last = ptr

            ptr = ptr.next

        return head

    def createList(self, l):
        head = ListNode(l[0])
        last = head

        for i in range(1, len(l)):
            new = ListNode(l[i])
            last.next = new
            last = new

        return head

    def viewList(self, l):
        while l:
            print(l.val, end=" ")
            l = l.next

s = Solution()

l = s.createList([1,1,1,2,2,3,3,3])
new = s.deleteDuplicates(l)
s.viewList(new)


