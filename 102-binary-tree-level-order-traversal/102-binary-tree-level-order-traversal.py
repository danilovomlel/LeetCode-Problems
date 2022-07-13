# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def CreateLevel(self, ParentLevel):
        ans = []
        for Node in ParentLevel:
            if Node.left:
                ans.append(Node.left)
            if Node.right:
                ans.append(Node.right)
        return ans
        
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not(root):
            return []
        
        ListNodes = [[root]]
        Children = [1]
        while(Children):
            Children = self.CreateLevel(ListNodes[-1])
            if len(Children)>0:
                ListNodes += [Children]
        
        level = []
        ans = []
        for LEVEL in ListNodes:
            for NODE in LEVEL:
                level.append(NODE.val)
            ans.append(level)
            level = []
            
        return ans
            
        
        
        
        