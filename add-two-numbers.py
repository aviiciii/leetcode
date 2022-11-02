# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1 , l2):
    x=''
    y=''
    while l1!=None:
        x+=str(l1.val)
        l1=l1.next

    while l2!=None:
        y+=str(l2.val)
        l2=l2.next
    # list is reversed
    x=x[::-1]
    y=y[::-1]

    # add and reverse
    sum = str(int(x) + int(y))[::-1]
    
    sum_list=None
    pointer=sum_list
    for digit in sum:
        if sum_list==None:
            sum_list=ListNode(digit)
            pointer=sum_list
        else:
            pointer.next=ListNode(digit)
            pointer=pointer.next
    return(sum_list)



l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

l = addTwoNumbers(l1,l2)


while l!=None:
    print(str(l.val),end='')
    l=l.next
