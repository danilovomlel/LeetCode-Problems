class Solution:
    
    def target(self, cur: Optional[TreeNode], tgt: int, branchNode: Optional[TreeNode]):
        
        if cur:
            if   cur.val==tgt and cur!=branchNode:
                return True
            elif cur.val>tgt:
                return self.target(cur.left, tgt, branchNode)
            elif cur.val<tgt:
                return self.target(cur.right, tgt, branchNode)
            else:
                return False
        else:
            return False
        
    
    def findTarget(self, cur: Optional[TreeNode], tgt: int) -> bool:
        
        try:
            self.k, k, root = self.k, self.k, self.root
        except AttributeError:
            self.root, self.k = cur, tgt
            k, root = self.k, self.root
            tgt = self.k - cur.val
        
        if cur:
            L, R = cur.left, cur.right
            tgtL = k - L.val if L else 0
            tgtR = k - R.val if R else 0        
            return self.target(root, tgt, cur) or self.findTarget(L, tgtL) or self.findTarget(R, tgtR)     
        else:
            return False
    

        

          
       
        
        
                    