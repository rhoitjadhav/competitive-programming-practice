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

def sortedInsert(head, data):
    new = DoublyLinkedListNode(0)
    new.next = head
    head.prev = new
    head = new
    last = head
    ptr = head.next
    new = DoublyLinkedListNode(data)
    while ptr:
        if ptr.data > data:
            ptr.prev.next = new
            new.prev = ptr.prev
            new.next = ptr
            ptr.prev = new
            return head.next
        
        last = ptr
        ptr = ptr.next

    last.next = new
    new.prev = last

    return head.next


ldata = [1, 2, 4]
data = 

llist = DoublyLinkedList()

for i in range(len(ldata)):
    llist.insert_node(ldata[i])

llist1 = sortedInsert(llist.head, data)
view_linkedlist(llist1)
