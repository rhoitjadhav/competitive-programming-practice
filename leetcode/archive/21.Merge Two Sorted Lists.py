# Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        output = None
        last = None
        s1_flag = None
        s2_flag = None
        s1 = l1
        s2 = l2

        while True:
            if s1 is None:
                s1_flag = True
                s2_flag = False
                break

            if s2 is None:
                s2_flag = True
                s1_flag = False
                break

            if s1.val == s2.val:
                new = ListNode(s1.val)
                new1 = ListNode(s2.val, new)

                if last is not None:
                    last.next = new1
                else:
                    output = new1

                s1 = s1.next
                s2 = s2.next

            elif s1.val < s2.val:
                new = ListNode(s1.val)

                if last is not None:
                    last.next = new
                else:
                    output = new

                s1 = s1.next

            else:
                new = ListNode(s2.val)

                if last is not None:
                    last.next = new
                else:
                    output = new

                s2 = s2.next

            last = new

        if s1_flag is False:
            while s1:
                new = ListNode(s1.val)
                last.next = new
                last = new
                s1 = s1.next

        if s2_flag is False:
            while s2:
                new = ListNode(s2.val)
                last.next = new
                last = new
                s2 = s2.next

        return output

    def mergeTwoLists1(self, l1, l2) -> ListNode:
        head = ListNode(0)
        last = head
        while True:
            if l1 is None:
                last.next = l2
                break

            elif l2 is None:
                last.next = l1
                break

            else:
                if l1.val < l2.val:
                    new = l1.val
                    l1 = l1.next

                else:
                    new = l2.val
                    l2 = l2.next

                new_node = ListNode(new)
                last.next = new_node
                last = last.next

        return head.next

    def view_list(self, l: ListNode):
        while l:
            print(l.val)
            l = l.next


s = Solution()

l1 = ListNode(1)
a = ListNode(2)
b = ListNode(4)
l1.next = a
a.next = b

l2 = ListNode(1)
a = ListNode(3)
b = ListNode(4)
l2.next = a
a.next = b

l = s.mergeTwoLists1(l1, l2)

s.view_list(l)
