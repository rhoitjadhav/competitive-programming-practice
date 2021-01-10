from collections import deque

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def levelOrder(root):
    global q
    q.append(root)
    while q:
        ele = q[0]
        print(ele.info)
        q.popleft()
        if ele.left is not None:
            q.append(ele.left)
        if ele.right is not None:
            q.append(ele.right)

    
    # print(root.info)
    # preOrder(root.left)
    # preOrder(root.right)


q = deque()
tree = BinarySearchTree()

arr = list(map(int, "1 2 5 3 6 4".split()))

for i in range(6):
    tree.create(arr[i])

levelOrder(tree.root)