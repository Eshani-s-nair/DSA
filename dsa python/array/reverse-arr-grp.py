#Reverse an Array in groups of given size
#https://www.geeksforgeeks.org/dsa/reverse-array-groups-given-size/
def reverse_arr(arr,k):
    n=len(arr)
    new_arr=[]
    for i in range(0,n,k):
        subarr=arr[i:i+k]
        subarr=subarr[::-1]
        for i in subarr:
            new_arr.append(i)
    return new_arr
print(reverse_arr([1,2,3,4,5,6,7,8,9],5))

#or
def reverse_arr(arr,k):
    n=len(arr)
    for i in range(0,n,k):
        arr[i:i+k]=arr[i:i+k][::-1]
    return arr
print(reverse_arr([1,2,3,4,5,6,7,8,9],5))

#or
def reverse_arr(arr,k):
    n=len(arr)
    for i in range(0,n,k):
        start=i
        end=min(i+k-1,n-1)
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    return arr
print(reverse_arr([1,2,3,4,5,6,7,8,9],5))