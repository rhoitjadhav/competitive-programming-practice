
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        print(node.data)
        node = node.next
        
def findMergeNode(head1, head2):
    ptr1 = head1
    ptr2 = head2 

    while True:
        if ptr1 == ptr2:
            return ptr1.data

        if ptr1 is None:
            ptr1 = head2
        
        if ptr2 is None:
            ptr2 = head1
        
        ptr1 = ptr1.next
        ptr2 = ptr2.next



