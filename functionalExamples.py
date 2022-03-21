from functools import *
from itertools import *
from operator import *
from collections import *

arr = list(range(20))

# print every element that is > than 4
def compareElem():
    print("> 4: ",[x for x in arr if x > 4])

# print if is even
def isEven():
    print("Even: ",[total for total in arr if total % 2 == 0]) 

# print the sum of arr elements
def sumArr():
    print("Sum: ",reduce(lambda total, i: total + i, arr)) 
    print("Sum: ",reduce(add, arr))

# print combination of arrays
def combinationArrs():
    x = [1, 2, 3]
    y = ['A', 'B']
    print("Combination: ",list(product(x, y)))

def reverseString():
    frase = "Eu sou muito top"
    fraseReversa = " ".join(frase.split()[::-1])
    print("Frase reversa: ",fraseReversa) 

def compareAnagrams():
    palavra = "banana"
    palavra2 = "aananb"
    if (Counter(palavra) == Counter(palavra2)):
        print("Banana: ", Counter(palavra))

        