# Find a value using DFS algorithm

from src.binaryTree import *

def createBT():
    root             = Node(1)
    root.left        = Node(2);
    root.right       = Node(3);
    root.left.left   = Node(4);
    root.left.right  = Node(5);
    root.right.right = Node(6);
    
    return root

def findValueRecursive(root, target):
    if (root is None): return False
    if (root.val == target): return True 
    return findValueRecursive(root.left, target) | findValueRecursive(root.right, target)

def findValue(root, target):
    if (root is None): return False
    
    queue = [root] 
    
    while(len(queue) > 0):
        current = queue.pop()
        if(current.val == target): return True
        if(current.left is not None): queue.append(current.left)
        if(current.right is not None): queue.append(current.right)
    

def main():
    root = createBT()
    if (findValueRecursive(root, 56)):
        print("Value exists in the tree")
    else:
        print("Value doesn't exist in the tree")

if __name__ == "__main__":
    main()

