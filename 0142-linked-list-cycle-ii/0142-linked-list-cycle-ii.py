# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return None
        # if(head== head.next.next):
        #     return head
        tp = {}
        # slow , fast = head ,head
        # while(fast.next and fast.next.next):
        #     if(slow.next == fast.next.next):
        #         return slow.next.next
        #     slow = slow.next
        #     fast = fast.next.next
        while head.next:
            if(head.next in tp):
                return head.next
            tp[head]=1
            head = head.next
        return None
        