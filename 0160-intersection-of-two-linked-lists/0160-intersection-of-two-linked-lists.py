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
        lt2 = []
        print(1)
        temp = headA
        tp = headB
        while(temp!=None):
            lt1.append(temp)
            temp = temp.next
        while(tp!=None):
            lt2.append(tp)
            tp = tp.next
        for i in lt1:
            if i in lt2:
                return i
#         while(headB!=None):
#             if(headB.next in lt):
#                 return headB.next
#             headB=headB.next
        