def merge(intervals):
    intervals.sort(key=lambda x: x[0]) #sort by firt element of array
    merged = []
    for i in intervals:
        if not merged or merged[-1][1] < i[0]: #if dont overlapping, just add the subarray
            merged.append(i)
        else: #otherwise change the last value from subarry for the max value (itself or the first value from the next subarray)
            merged[-1][1] = max(merged[-1][1], i[1])
    print(merged)
 
arr = [[1,3],[2,5],[6,9]]
merge(arr)
