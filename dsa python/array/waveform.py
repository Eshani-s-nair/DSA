#Sort an array in wave form
#Given a sorted array of integers, sort the array in a wave form. An array ‘arr[0..n-1]’ is in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4]….
#https://www.geeksforgeeks.org/dsa/sort-array-wave-form/

def wave_form(arr):
    n=len(arr)
    for i in range(0,n-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
print(wave_form( [2, 4, 7, 8, 9, 10]))