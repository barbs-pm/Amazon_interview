from src.binaryTree import *


def createBT():
    root             = Node(1)
    root.left        = Node(2);
    root.right       = Node(3);
    root.left.left   = Node(4);
    root.left.right  = Node(5);
    root.right.right = Node(6);
    
    return root

def findValue():
    

root = createBT
findValue(root)