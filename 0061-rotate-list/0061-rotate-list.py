# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None):
            return head
        sz = 1
        dummy = head
        while dummy.next:
            dummy =dummy.next
            sz+=1
        if(k>sz):
            k = k % sz
        if(k==sz or k==0):
            return head
        k = sz - k
        break_node = head
        while(k>1):
            k-=1
            break_node = break_node.next
        new_head = break_node.next
        break_node.next = None
        join = new_head
        while join.next:
            join = join.next
        join.next = head
        return new_head
        
        
        
            

        
            
        