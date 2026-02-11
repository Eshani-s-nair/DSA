def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        smallest=i
        for j in range(i+1,n):
            if arr[smallest]>arr[j]:
                smallest=j
        min_value=arr.pop(smallest)
        arr.insert(i,min_value)
    return arr
s=selection_sort([7,12,9,11,3])            
print(s)
            