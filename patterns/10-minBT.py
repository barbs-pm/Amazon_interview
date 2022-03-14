# Find the min value from tree using DFS algorithm

from src.binaryTree import *

def createBT():
    root             = Node(1)
    root.left        = Node(-2);
    root.right       = Node(3);
    root.left.left   = Node(4);
    root.left.right  = Node(-5);
    root.right.right = Node(6);
    
    return root

def sumNodesRecursive(root):
    if (root is None): return False

    leftValues = sumNodesRecursive(root.left)
    rightValues = sumNodesRecursive(root.right)
    
    return min(root.val, leftValues, rightValues)

def sumNodes(root):
    if (root is None): return False

    queue = [root]
    minValue = root.val

    while(len(queue) > 0):
        current = queue.pop()
        
        if(current.val < minValue): minValue = current.val
        if(current.left is not None): queue.append(current.left)
        if(current.right is not None): queue.append(current.right)
        
    return minValue

def main():
    root = createBT()
    print(sumNodesRecursive(root))

if __name__ == "__main__":
    main()

