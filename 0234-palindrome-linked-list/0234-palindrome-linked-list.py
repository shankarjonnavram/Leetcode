# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next==None):
            return True
        slow , fast = head , head
        ct =0
        lt = []
        while(fast.next!=None and fast.next.next!=None):
            lt.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            ct+=1
        if(fast.next!=None):
            lt.append(slow.val)
            ct+=1
        while(slow.next!=None):
                slow = slow.next
                if(slow.val!=lt[ct-1]):
                    return False
                ct-=1
        return True
            
            