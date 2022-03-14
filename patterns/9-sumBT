# Sum all nodes from tree using DFS algorithm

from src.binaryTree import *

def createBT():
    root             = Node(1)
    root.left        = Node(2);
    root.right       = Node(3);
    root.left.left   = Node(4);
    root.left.right  = Node(5);
    root.right.right = Node(6);
    
    return root

def sumNodesRecursive(root):
    if (root is None): return 0
    return root.val + sumNodesRecursive(root.left) + sumNodesRecursive(root.right)

def sumNodes(root):
    if (root is None): return 0
    
    queue = [root]
    sumNodes = 0

    while(len(queue) > 0):
        current = queue.pop()
        sumNodes += current.val

        if(current.left is not None): queue.append(current.left)
        if(current.right is not None): queue.append(current.right)

    return sumNodes

def main():
    root = createBT()
    print(sumNodesRecursive(root))

if __name__ == "__main__":
    main()

