# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        Nodes = []
        if not(head):
            return head
        
        while(head.next):
            Nodes.append(head)
            if head.next in Nodes:
                return head.next
            head = head.next
        return head.next
            