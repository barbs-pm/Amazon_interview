 # Max Root to Leaf Path Sum
 # Find the min value from tree using DFS algorithm

from src.binaryTree import *

def createBT():
    root             = Node(3)
    root.left        = Node(-2);
    root.right       = Node(3);
    root.left.left   = Node(4);
    root.left.right  = Node(-5);
    root.right.right = Node(6);
    
    return root

def sumPathRecursive(root):
    if (root is None): return -float('Inf')
    if(root.left is None and root.right is None): return root.val
    
    maxValue = max(sumPathRecursive(root.left),sumPathRecursive(root.right))
    
    return root.val + maxValue

def main():
    root = createBT()
    print(sumPathRecursive(root))

if __name__ == "__main__":
    main()

