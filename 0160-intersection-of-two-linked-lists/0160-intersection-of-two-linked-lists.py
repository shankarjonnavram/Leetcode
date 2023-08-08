# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if(headA==headB):
        #     return headB
        lt1 = []
        temp = headA
        tp = headB
        while(temp!=None):
            lt1.append(temp)
            temp = temp.next
        while(tp!=None):
            if tp in lt1:
                return tp
            tp = tp.next

        