# Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
# Consider two sorted linked lists and the merged list below them as an example.
# head1 -> 4 -> 8 -> 15 -> 19 -> NULL
# head2 -> 7 -> 9 -> 10 -> 16 -> NULL
# head1 -> 4 -> 7 -> 8 -> 9 -> 10 -> 15 -> 16 -> 19 -> NULL
from linked_list import *


def merge_sorted(head1, head2):

    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None;
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead
    
    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp
        
    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    #mergedHead.listprint()
    return mergedHead

n0 = Node(4)
n1 = Node(8)
n2 = Node(15)
n3 = Node(19)
n4 = Node(22)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

m0 = Node(7)
m1 = Node(9)
m2 = Node(10)
m3 = Node(16)
m0.next = m1
m1.next = m2
m2.next = m3

merge_sorted(n0,m0)
