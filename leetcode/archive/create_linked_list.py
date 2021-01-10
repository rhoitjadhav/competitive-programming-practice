class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createList(self, l):
    head = ListNode(l[0])
    last = head

    for i in range(1, len(l)):
        new = ListNode(l[i])
        last.next = new
        last = new

    return head
