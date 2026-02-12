#https://www.geeksforgeeks.org/dsa/program-to-reverse-an-array/
def reverse_array(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
print(reverse_array([1,2,3,4,5]))

#or
def reverse_array(arr):
    return arr[::-1]
print(reverse_array([1,2,3,4,5]))
