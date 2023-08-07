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
        
        # tmp = head
        # rem = head
        # ct = 0 
        # while(tmp!=None):
        #     temp_ct = n
        #     tmp = tmp.next
        #     ct+=1
        # n = ct - n 
        # if(n==0):
        #     return head.next
        # old = None
        # while(n>0):
        #     old = rem
        #     rem = rem.next
        #     n-=1
        # old.next = rem.next
        # return head
        
        fast = head
        slow = head
        
        # First moving fast pointer by n points . Thne moving both fast and slow                 pointers by one point each
        
        for i in range(n):
            fast = fast.next
        if(fast == None):
            return slow.next
        while(fast.next!=None):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
            
        
            
                