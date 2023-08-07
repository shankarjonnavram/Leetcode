# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # res = head
        # tmp = head
        # prev_node , next_node = None , None
        # while(tmp!=None):
        #     next_node = tmp.next
        #     tmp.next = prev_node
        #     prev_node = tmp
        #     tmp = next_node
        # # tmp is in none
        # while(n>1):
        #     tmp = prev_node
        #     prev_node = prev_node.next
        #     n-=1
        # tmp.next = prev_node.next
        # prev_node.next = None
        # return head
        
        tmp = head
        rem = head
        ct = 0 
        while(tmp!=None):
            tmp = tmp.next
            ct+=1
        n = ct - n 
        if(n==0):
            return head.next
        old = None
        while(n>0):
            old = rem
            rem = rem.next
            n-=1
        old.next = rem.next
        return head
            
        
            
                