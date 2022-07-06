# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        
        def h_tree(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            ans = False
            if root.val == subRoot.val:
                ans = try_subtree(root, subRoot)
            if root.left:
                ans = ans or h_tree(root.left, subRoot)
            if root.right:
                ans = ans or h_tree(root.right, subRoot)
            return ans
        
        def try_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            is_subtree = True
            
            if root.val == subRoot.val:
                if not(root.left or root.right):
                    if subRoot.left or subRoot.right:
                        return False
                elif root.left and not (root.right):
                    if subRoot.left and not (subRoot.right):
                        is_subtree = try_subtree(root.left, subRoot.left)
                    else:
                        return False
                elif root.right and not (root.left):
                    if subRoot.right and not (subRoot.left):
                        is_subtree = try_subtree(root.right, subRoot.right)
                    else:
                        return False
                else:
                    if subRoot.right and subRoot.left:
                        is_subtree = try_subtree(root.right, subRoot.right)           
                        is_subtree = try_subtree(root.left, subRoot.left) and is_subtree
                    else:
                        return False
            else:
                return False                
            return is_subtree
        
        ans = h_tree(root, subRoot)      
        return ans

        