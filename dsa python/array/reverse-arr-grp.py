#Reverse an Array in groups of given size
#https://www.geeksforgeeks.org/dsa/reverse-array-groups-given-size/
def reverse_arr(arr,k):
    n=len(arr)
    new_arr=[]
    for i in range(0,n,k):
        subarr=arr[i:i+k]
        print(subarr)
        subarr=subarr[::-1]
        for i in subarr:
            new_arr.append(i)
    return new_arr
print(reverse_arr([1,2,3,4,5,6,7,8,9],5))
