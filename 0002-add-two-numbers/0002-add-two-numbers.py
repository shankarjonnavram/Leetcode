# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra_val = 0
        lt = []
        head = l1
        old = None
        while(l1!=None and l2!=None):
            old = l1
            each_sum = extra_val + l1.val + l2.val
            if(each_sum >= 10):
                l1.val = each_sum - 10
                extra_val = 1
            else:
                l1.val = each_sum
                extra_val = 0
            l1 = l1.next
            l2 = l2.next
        while(l1!=None):
            old = l1
            each_sum = extra_val + l1.val
            if(each_sum >= 10):
                l1.val = each_sum - 10
                extra_val = 1
            else:
                l1.val = each_sum
                extra_val = 0
            l1 = l1.next
        while(l2!=None):
            each_sum = extra_val + l2.val
            print(each_sum)
            if(each_sum >= 10):
                temp_val = each_sum - 10
                old.next = ListNode(temp_val)
                extra_val = 1
                old = old.next
            else:
                old.next = ListNode(each_sum)
                extra_val = 0
                old = old.next
            l2 = l2.next
        if(extra_val > 0):
            old.next = ListNode(extra_val)
        return head