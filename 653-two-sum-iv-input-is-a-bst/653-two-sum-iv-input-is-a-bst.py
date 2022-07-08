class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        remaining = set()
        
        def traversal(node):
            if not node:
                return False
            if k - node.val in remaining:
                return True
            remaining.add(node.val)
            return traversal(node.left) or traversal(node.right)
        
        return traversal(root)
        

          
       
        
        
                    