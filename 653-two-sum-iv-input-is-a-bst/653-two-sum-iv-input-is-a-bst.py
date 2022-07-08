class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.root, self.k = root, k        
        return self.SearchTree(root, 0)
        
    def target(self, cur: Optional[TreeNode], tgt: int):
        branch = self.branch
        
        if cur.val==tgt and cur!=branch:
            return True
        elif cur.val>tgt and cur.left:
            return self.target(cur.left, tgt)
        elif cur.val<tgt and cur.right:
            return self.target(cur.right, tgt)
        else:
            return False
    
    def SearchTree(self, cur: Optional[TreeNode], tgt: int):
        root, k = self.root, self.k
        self.branch = cur
        
        if cur == root:
            tgt = k - root.val
        
        if not(cur.left or cur.right):
            return self.target(root, tgt)
        
        elif cur.left and cur.right:
            return self.target(root, tgt) or self.SearchTree(cur.left, k-cur.left.val) or self.SearchTree(cur.right, k-cur.right.val)

        elif cur.left:
            return self.target(root, tgt) or self.SearchTree(cur.left, k-cur.left.val)
            
        else:
            return self.target(root, tgt) or self.SearchTree(cur.right, k-cur.right.val)
          
       
        
        
                    