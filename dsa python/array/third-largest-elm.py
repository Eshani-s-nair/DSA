#https://www.geeksforgeeks.org/dsa/third-largest-element-array-distinct-elements/
def third_largest(arr):
    if len(arr)<3:
        return "Array should have atleast 3 elements"
    largest=second_largest=third_largest=float('-inf')
    for i in arr:
        if i>largest:
            third_largest=second_largest
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            third_largest=second_largest
            second_largest=i    
        elif i>third_largest and i!=second_largest and i!=largest:
            third_largest=i    
    return third_largest
print(third_largest([10, 5, 8, 20, 15]))

#or

def third_largest(arr):
    if len(arr)<3:
        return "Array should have atleast 3 elements"
    arr.sort()
    return arr[-3]
print(third_largest([10, 5, 8, 20, 15]))