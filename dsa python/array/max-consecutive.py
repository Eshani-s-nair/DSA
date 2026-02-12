#Maximum consecutive one’s (or zeros) in a binary array
#https://www.geeksforgeeks.org/dsa/maximum-consecutive-ones-zeros-binary-array/
def max_consecutive(arr):
    count=0
    max_count=0
    for i in arr:
        if i==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    return max(max_count,count)
print(max_consecutive([1,1,0,1,1,1,0,1]))
