# Singly Linked List with insertion and print methods
from src.linkedList import *


def reverseRecursive(LL, prev):
    
    # if its the end of the linked list
    if LL.next is None:
        LL.head = LL # set head as the current node
        LL.next = prev # his next its now his previous
        return

    next = LL.next
    LL.next = prev

    reverseRecursive(next, LL)

def reverse(LL):
    if LL.head is None:
        return
    reverseRecursive(LL.head, None)

LL = LinkedList()
for i in range(5):
    LL.insert(i)

print('Before reverse: ')
LL.printLL()
reverse(LL)
print('After reverse: ')
LL.printLL()

   