class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

   def listprint(self, nome):
      printval = self
      a = nome
      while printval is not None:
         a += " -> " + str(printval.data)
         printval = printval.next
      print(a)

class SLinkedList:
   def __init__(self, data=None):
      self.data = data
      self.next = None

