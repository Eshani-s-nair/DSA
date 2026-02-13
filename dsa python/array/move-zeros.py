#Move all Zeros to End of Array
#Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same.
#https://www.geeksforgeeks.org/dsa/move-zeros-end-array/
def move_zeros(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<len(arr):
        arr[count]=0
        count+=1
    return arr
print(move_zeros([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]))