#https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/

def second_largest(arr):
    if len(arr)<2:
        return "Array should have atleast 2 elements"
    largest=second_largest=float('-inf')
    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i    
    return second_largest
print(second_largest([10, 5, 8, 20, 15]))

#or 

def second_largest(arr):
    if len(arr)<2:
        return "Array should have atleast 2 elements"
    arr.sort()
    return arr[-2]
print(second_largest([10, 5, 8, 20, 15]))
  