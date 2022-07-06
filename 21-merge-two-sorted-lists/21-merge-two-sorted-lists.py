# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ans = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                ans.next = list1
                list1, ans = list1.next, list1
            else:
                ans.next = list2
                list2, ans = list2.next, list2
                
        if list1 or list2:
            ans.next = list1 if list1 else list2                  
        
        return head.next
        