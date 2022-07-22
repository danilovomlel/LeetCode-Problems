"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        try:
            self.traversal = self.traversal
        except AttributeError:
            if not root:
                return []
            else:
                self.traversal = []
        
        self.traversal.append(root.val)
        
        if not root.children:
            pass
        else:
            for node in root.children:
                self.preorder(node)            
        
        return self.traversal
        