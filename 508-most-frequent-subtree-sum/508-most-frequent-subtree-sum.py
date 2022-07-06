# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:      
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def inc_item(item: int):
            if item in freq.keys():
                freq[item] +=1
            else:
                freq[item] = 1
        def treesum(root: Optional[TreeNode]):

            if root.left and root.right:
                treesum(root.left)
                treesum(root.right)
                root.val += root.left.val + root.right.val
            elif root.left and not(root.right):
                treesum(root.left)
                root.val += root.left.val
            elif root.right and not(root.left):
                treesum(root.right)
                root.val += root.right.val
            inc_item(root.val)
            
        treesum(root)        
        
        max_key = max(freq, key = freq.get)
        max_freq = [k for k,v in freq.items() if v == freq[max_key]]
        return max_freq
        