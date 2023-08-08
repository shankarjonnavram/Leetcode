# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return None
        dummy = head
        slow , fast = head ,head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                #break
                while(head!=slow):
                    head = head.next
                    slow = slow.next
                return head
        # if(fast.next==None or fast.next.next==None):
        #     return None
        # while(head!=slow):
        #     head = head.next
        #     slow = slow.next
        # return head
        return None
        