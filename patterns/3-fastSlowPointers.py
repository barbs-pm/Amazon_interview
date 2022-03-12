# Given a linked list, determine if it has a cycle in it

# If the Linked Lists does not have a cycle in it, fast wiLL reach the end of the Linked Lists before the slow 
# and this wiLL reveal that there is no cycle in the Linked Lists. If slow reach fast, there's a cycle

from src.linkedList import *
 
def mid(LL):
    fast = slow = LL

    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if (fast == slow):
            print("There's a cycle in the list")
            return 0

    print("There isn't a cycle in the list")
    return slow

LL = LinkedList()
for i in range(10):
    LL.insert(i)

midNode = mid(LL.head)
print(midNode.data) 