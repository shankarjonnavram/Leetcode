# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # if(headA==headB):
        #     return headB
        # lt1 = {}
        # temp = headA
        # tp = headB
        # while(temp!=None):
        #     lt1[temp] = 1
        #     temp = temp.next
        # while(tp!=None):
        #     if tp in lt1:
        #         return tp
        #     tp = tp.next
        d1 = headA
        d2 = headB
        while(d1!=d2):
            d1 = d1.next
            d2 = d2.next
            if(d1==None and d2==None):
                return d1
            elif(d1==None):
                d1=headB
            elif(d2==None):
                d2 = headA
        return d1

        