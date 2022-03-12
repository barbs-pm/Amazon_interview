from src.linkedList import *

def reverseRecursive(curr, prev):
    
    # if its the end of the linked list
    if curr.next is None:
        linkedList.head = curr
        reversedList = linkedList.head
        reversedList.next = prev

        return

    next = curr.next
    curr.next = prev

    reverseRecursive(next, curr)

def reverse(linkedList):
    if linkedList is None:
        return
    reverseRecursive(linkedList.head, None)

linkedList = LinkedList()
for i in range(5):
    linkedList.insert(i)

print('Before reverse: ')
linkedList.printLL()
reverse(linkedList)
print('After reverse: ')
linkedList.printLL()

   