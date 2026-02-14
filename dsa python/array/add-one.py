#Adding one to number represented as array of digits
#https://www.geeksforgeeks.org/dsa/adding-one-to-number-represented-as-array-of-digits/
def add_one(arr):
    str1=""
    for i in arr:
        str1+=str(i)
    str1=int(str1)+1
    return str1
print(add_one([1,2,3]))

#or
def add_one(arr):
    carry=1
    n=len(arr)
    for i in range(n-1,-1,-1):
        sum=arr[i]+carry
        arr[i]=sum%10
        carry=sum//10
    
    if carry:
        arr.insert(0,carry)
    for i in arr:
        print(i,end="")
add_one([9,9,9])
print(" ")

#or 
def add_one(arr):
    n=len(arr)
    i=n-1
    while i>=0 and arr[i]==9:
        arr[i]=0
        i-=1
    if i<0:
        arr.insert(0,1)
    else:
        arr[i]+=1
    for i in arr:
        print(i,end="")
add_one([9,9,9])
print(" ")
add_one([1,2,3])
