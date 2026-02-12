#Rotate an Array by d - Counterclockwise or Left
#https://www.geeksforgeeks.org/dsa/rotate-array-d-left-rotation/
def rotate_arr(arr,d):
    n=len(arr)
    d=d%n
    return arr[d:]+arr[:d]
print(rotate_arr([1,2,3,4,5],8))


#or 
def rotate_arr(arr,d):
    n=len(arr)
    for i in range(d):
        x=arr.pop(0)
        arr.insert(n-1,x)
    return arr
print(rotate_arr([1,2,3,4,5],8))