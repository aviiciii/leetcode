# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
    prev = None
    i = head

    while i != None:
        front = i.next
        i.next = prev
        prev = i
        i = front
    return prev

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, mid = head, head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            mid = mid.next
            
        new = reverse_list(mid.next)

        i = head
        j = new
        while j!= None:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True


        # while slow.next!= None:
        #     fast = fast.next
        #     slow = slow.next
        #     if fast.val != slow.val:
        #         return False

        # return True