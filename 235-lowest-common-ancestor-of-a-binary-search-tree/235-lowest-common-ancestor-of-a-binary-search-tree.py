# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p.val > q.val:    #Garantir p.val < q.val
            aux = p
            p = q
            q = aux
            
        while True:
            if (root.val>p.val and root.val<q.val) or (root==p) or (root==q):
                break
                
            if root.val>q.val:
                root = root.left
            elif root.val<p.val:
                root = root.right
         
        
        return root
        