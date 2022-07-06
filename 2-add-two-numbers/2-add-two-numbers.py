# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        dig1 = 0
        dig2 = 0
        vai_um = 0
        
        while l1.next or l2.next:
            dig1 = l1.val
            dig2 = l2.val

            soma = dig1 + dig2 + vai_um
            ans.val = soma % 10        
            vai_um = 0
            if soma > 9:
                vai_um = 1
            
            if not(l1.next):
                l1.val = 0
            if l1.next:
                l1 = l1.next
            
            if not(l2.next):
                l2.val = 0
            if l2.next:
                l2 = l2.next
            ans.next = ListNode()
            ans = ans.next
            
        dig1 = l1.val
        dig2 = l2.val

        soma = dig1 + dig2 + vai_um
        ans.val = soma % 10
        if soma > 9:
            ans.next = ListNode()
            ans = ans.next
            ans.val = 1
        
        return head
    
            
            

        