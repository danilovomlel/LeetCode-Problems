
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sz = 1
        dmy = ListNode()
        dmy.next = head
        
        while(head.next):
            sz+= 1
            head = head.next
        
        sz=int(sz/2)
        
        while(sz):
            sz-= 1
            dmy = dmy.next
        
        return dmy.next
        