from functools import *
from itertools import *
from operator import *

arr = list(range(20))

# print every element that is > than 4
print("> 4: ",[x for x in arr if x > 4])

# print if is even
print("Even: ",[total for total in arr if total % 2 == 0]) 

# print the sum of arr elements
print("Sum: ",reduce(lambda total, i: total + i, arr)) 
print("Sum: ",reduce(add, arr))

# print combination of arrays
x = [1, 2, 3]
y = ['A', 'B']
print("Combination: ",list(product(x, y)))

def addcount(counter, element):
    if element not in counter:
        counter[element] = 1
    else:
        counter[element] += 1
    return counter

items = ["a", "b", "a", "c", "d", "c", "b", "a"]
print("Qnt: ", reduce(addcount, items, {}))