# Same Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None: return True
        if p is None or q is None: return False
        return self.dfs(p, q)

    def dfs(self, root, root1):
        if root and root1: 
  
            # First print the data of node 
            print(root.val, root1.val), 
            if root.val != root1.val:
                return False
    
            # Then recur on left child 
            if not self.dfs(root.left, root1.left): return False
    
            # Finally recur on right child 
            if not self.dfs(root.right, root1.right): return False

        
        if root and root1 is None: return False
        elif root1 and root is None: return False
        else: return True

    def createList(self, l):
        pass
    

s = Solution()

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2))

# s.isSameTree()
print(s.dfs(p, q))
