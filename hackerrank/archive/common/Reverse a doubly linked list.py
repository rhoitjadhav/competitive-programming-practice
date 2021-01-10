class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def view_linkedlist(head):
    while head:
        print(head.data, end=' ')
        head = head.next


def reverse(head):
    new = DoublyLinkedListNode(-1)
    new.next = head
    head.prev = new
    head = new
    ptr = head.next
    last = head

    result = DoublyLinkedList()

    while ptr:
        last = ptr
        ptr = ptr.next

    ptr = last
    while ptr:
        if ptr.data == -1:
            break
        result.insert_node(ptr.data)
        ptr = ptr.prev

    return result.head


ldata = [1, 2, 4]

llist = DoublyLinkedList()

for i in range(len(ldata)):
    llist.insert_node(ldata[i])

llist1 = reverse(llist.head)
view_linkedlist(llist1)
