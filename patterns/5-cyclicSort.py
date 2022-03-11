# This approach is quite useful when dealing with numbers in a given range and asking to find the duplicates/missing ones etc.
# When the problem involving arrays containing numbers in a given range, you should think about Cyclic Sort pattern.

def missingNumber(arr):
    start = 0

    while start < len(arr):
        num = arr[start]
        if num < len(arr) and num != start: # if the value isnt in the right place
            arr[start], arr[num] = arr[num], arr[start] # change between values
        else: # its in the right place, go to the next
            start += 1

    for i in range(len(arr)):
        if arr[i] != i: # if value doesnt correspond to his index
            print("Missing number:",i) # the index is the missed one
            return 0
    
    print("Sorted array:",arr)

arr = [0,4,1,3]
missingNumber(arr)