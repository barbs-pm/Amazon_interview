# Given a linked list, determine if it has a cycle in it

# If the Linked Lists does not have a cycle in it, fast will reach the end of the Linked Lists before the slow 
# and this will reveal that there is no cycle in the Linked Lists. If slow reach fast, there's a cycle

class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.nextNode = nextNode
 
    def addNode(self, val):
        newNode = Node(val)
        self.nextNode = newNode
        return newNode

head = Node(1) # create the linked list
p = head

for i in range(2, 10): #insert nodes
    p = p.addNode(i)
 
def mid(head):
    fast = slow = head

    while(fast is not None and fast.nextNode is not None):
        fast = fast.nextNode.nextNode
        slow = slow.nextNode
        if (fast == slow):
            print("There's a cycle in the list")
            return 0

    print("There isn't a cycle in the list")
    return slow

midNode = mid(head)
print(midNode.val) 