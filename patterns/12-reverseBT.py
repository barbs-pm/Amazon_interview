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

def reverseBinTree(root):
    
    if root == None: return

    temp = root.left
    root.left = root.right
    root.right = temp
    
    map(reverseBinTree, (root.left, root.right))

    return root
    
def print_tree(root) : 
  
    if (root == None):  
        return
          
    print (root.val)
    print_tree(root.left)  
    print_tree(root.right)  

def main():
    root = createBT()
    reverseBinTree(root)
    print_tree(root)

if __name__ == "__main__":
    main()

