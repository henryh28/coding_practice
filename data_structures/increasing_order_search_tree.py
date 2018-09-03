class Solution:
    
    # Use In-order traversal to check left child-> right child -> parent
    def increasingBST(self, root, parent = None):
        # Triggered when run from 'None' children nodes
        if not root:
          return parent
        
        # Recursively calls self down to left-most nodes, if exists
        node = self.increasingBST(root.left, root)
        
        # Recursively set all left children nodes to 'None'
        root.left = None
        
        # Calls next available right child node, which will then check all left child nodes
        root.right = self.increasingBST(root.right, parent)
        return node
        