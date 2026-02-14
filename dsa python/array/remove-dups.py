#Remove duplicates from Sorted Array
#https://www.geeksforgeeks.org/dsa/remove-duplicates-sorted-array/
def remove_dups(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1]==arr[i]:
            arr.pop(i)
    return arr
print(remove_dups([2,2,3,4,4]))