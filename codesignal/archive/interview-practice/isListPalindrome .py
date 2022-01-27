# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def reverse(head):
    n = head
    r = None
    temp = None

    while n:
        # Move forward
        temp = n
        n = n.next

        # Join
        temp.next = r
        r = temp

    return temp


def solution(head):
    ptr = head
    count = 0
    while ptr:
        ptr = ptr.next
        count += 1

    if count < 2:
        return True
    mid = (count - 1) // 2

    ptr = head
    while mid:
        ptr = ptr.next
        mid -= 1

    ptr1 = reverse(ptr.next)
    ptr = head
    while ptr1:
        if ptr.value != ptr1.value:
            return False
        ptr = ptr.next
        ptr1 = ptr1.next

    return True
