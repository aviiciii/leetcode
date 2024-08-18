# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head:
        
            head2 = head.next
        else:
            return head

                
        i1 = head
        if i1.next != None:
            i2 = i1.next.next

        j1 = head2
        if j1:
            if j1.next != None:
                j2 = j1.next.next
        else:
            return head

        while i2 != None:
            
            i1.next = i2

            if j1!= None:
                j1.next = j2
            
            
            if i2 != None and i2.next!=None:
                i2 = i2.next.next
            else:
                i2 = None
            

            if j2 != None and j2.next!=None:
                j2 = j2.next.next
            else:
                j2 = None

            i1 = i1.next
            if j1 != None:
                j1 = j1.next
        i1.next = head2

        return head