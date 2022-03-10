#searching pairs in a sorted array

def isPairSum(arr, lenA, val):
    i = 0        #first pointer
    j = lenA - 1 #second pointer

    while (i < j):
        if (arr[i] + arr[j] == val): #if find a pair, return
            print("Pair:",arr[i], arr[j])
            return True
        elif (arr[i] + arr[j] < val): #if val is bigger, go to the next 
            i += 1
        else: #if the sum of elements is more, move towards lower values
            j -= 1
    return 0

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17
 
print(isPairSum(arr, len(arr), val))