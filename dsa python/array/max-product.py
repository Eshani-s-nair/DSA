#Maximum product of a triplet (subsequence of size 3) in array
#https://www.geeksforgeeks.org/dsa/maximum-product-triplet-subsequence-size-3-array/
def max_product(arr):
    arr.sort()
    return arr[-1]*arr[-2]*arr[-3]
print(max_product([10,-10,5,2]))