# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None or head.next==None):
            return False
        slow , fast = head ,head
        # while(slow!=None and fast!=None):
        #     slow = slow.next
        #     if(fast.next == None):
        #         return False
        #     fast = fast.next.next
        #     if(slow==fast):
        #         return True
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False
            
        