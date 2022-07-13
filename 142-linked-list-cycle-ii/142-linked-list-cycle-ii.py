# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Otimo em tempo gasta mais memoria
        #Nodes = []
        #if not(head):
        #    return head
        #
        #while(head.next):
        #    Nodes.append(head)
        #    if head.next in Nodes:
        #        return head.next
        #    head = head.next
        #return head.next
        
        #Otima em memoria gasta mais tempo
        if not(head):
            return head
        elif not(head.next):
            return head.next
        
        slow = head
        faster = head.next
        count_cycle = 0
        
        while(slow!=faster and faster.next):
            slow = slow.next
            if faster.next.next:
                faster = faster.next.next
            else:
                return faster.next.next
            
            if slow==faster:
                faster = faster.next
                count_cycle = 1
                while(slow!=faster):
                    slow = slow.next
                    faster = faster.next.next
                    count_cycle += 1
        
        if not(faster.next):
            return faster.next
                    
        #count_cycle contem o numero de Node no ciclo
        while(head!=slow):
            for i in range(count_cycle):
                slow = slow.next
                if slow==head:
                    return head
            head = head.next
            
        return head
        
        
        