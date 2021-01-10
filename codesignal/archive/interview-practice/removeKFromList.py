# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def removeKFromList(head, k):
    last = ListNode(-1, head)
    head = last
    ptr = head.next

    while ptr:
        if ptr.value == k:
            last.next = ptr.next
        else:
            last = ptr
        ptr = ptr.next

    return head.next
