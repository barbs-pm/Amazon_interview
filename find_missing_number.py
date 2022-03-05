#You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. 
# The input array is not sorted. Look at the below array and give it a try before checking the solution.
# 3 | 7 | 1 | 2 | 8 | 4 | 5  -> n = 8, number missing = 6

def find_missing(input):
    
    n = len(input) + 1
    sum_of_elements = sum(input)
    expected_sum = (n / 2) * (1 + n)

    return (expected_sum - sum_of_elements)

find_missing([3,7,1,2,8,4,5])