class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def view_list(self):
        temp = self.head
        
        while(temp):
            print(str(temp.data), end=" | ")
            temp = temp.next

    def add_element(self):
        postion = input("\nAdd: \n1. Front \n2. Middle \n3. End \nSelect Postion: ")
        data = input("Enter Data: ")
        new_node = Node(data)
        temp = self.head

        if postion == "1":
            if self.head is None:
                self.head = Node(data)
            
            else:
                new_node.next = self.head
                
                self.head = new_node

        
        elif postion == "2":
            middle_pos = int(input("Enter Middle Position: "))

            index = 1
            while(temp):
                if middle_pos - 1 == index:
                    new_node.next = temp.next
                    temp.next = new_node
                    break

                temp = temp.next
                index += 1
            
        elif postion == "3":
            while(temp):
                if temp.next is None:
                    temp.next = new_node
                    break
                
                temp = temp.next
        
        else:
            print("Invalid Input")

    def remove_element(self):
        postion = input("Remove: \n1. Front \n2. Middle \n3. End \nSelect Postion: ")
        temp = self.head

        if postion == "1":
            if self.head is None:
                print("Linked list is empty")
            
            else:
                self.head = self.head.next
                
        elif postion == "2":
            middle_pos = int(input("Enter Middle Position: "))
            index = 1
            while(temp):
                if middle_pos - 1 == index:
                    temp.next = temp.next.next
                    break

                temp = temp.next

        elif postion == "3":
            while(temp):
                if temp.next.next is None:
                    temp.next = None
                    break

                temp = temp.next
        
        else:
            print("Invalid input")


if __name__ == "__main__":
    single_list = SingleLinkedList()
    
    # single_list.head = Node(10)
    # second = Node(20)
    # single_list.head.next = second

    single_list.add_element()
    single_list.view_list()
    single_list.add_element()
    single_list.view_list()
    single_list.add_element()
    single_list.view_list()
    single_list.remove_element()
    single_list.view_list()
