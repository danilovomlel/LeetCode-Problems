# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not(head):
            return head
        if not(head.next):
            return head
        else:            
            dmy, dmy2 = ListNode(), ListNode()
            dmy.next, cur = head, head.next
            dmy2.next = cur
            head.next = None
            
            while(cur.next):                
                dmy2.next = cur.next
                cur.next = dmy.next
                dmy.next = cur
                cur = dmy2.next
                
            dmy2.next.next = dmy.next   
            return dmy2.next

        
            
            
            
            
            
        