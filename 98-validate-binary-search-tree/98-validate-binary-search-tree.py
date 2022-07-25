# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidSubTree(self, root: Optional[TreeNode]) -> tuple:
        
        ans, MIN, MAX = True, 0, 0        
        if root.left:
            is_L_Tree, L_MIN, L_MAX = self.isValidSubTree(root.left)
        else:
            is_L_Tree, L_MIN, L_MAX = True, None, None
            
        if root.right:
            is_R_Tree, R_MIN, R_MAX = self.isValidSubTree(root.right)
        else:
            is_R_Tree, R_MIN, R_MAX = True, None, None
            
        if is_L_Tree and is_R_Tree:
            if not(L_MAX):
                MIN = root.val
            elif L_MAX < root.val:
                MIN = L_MIN
                ans = True
            else:
                ans = False
                
            if not(R_MIN):
                MAX = root.val
            elif R_MIN > root.val:
                MAX = R_MAX
                ans = True and ans
            else:
                ans = False
        else:
            ans = False
            
        return ans, MIN, MAX
        
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = self.isValidSubTree(root)
        return ans[0]
        
        
        