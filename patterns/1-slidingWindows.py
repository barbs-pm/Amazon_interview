# when to use:  
# the problem asks to find the maximum (or minimum) value for a function that calculates the answer 
# repeatedly for a set of ranges from the array

def maxSum(arr, k):
    n = len(arr)
    sumSubArr = sum(arr[:k])
    max_sum = sumSubArr
 
    for i in range(n - k):
        sumSubArr = sumSubArr - arr[i] + arr[i + k]
        max_sum = max(sumSubArr, max_sum)
 
    return max_sum
 
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))