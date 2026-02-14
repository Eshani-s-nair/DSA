#Stock Buy and Sell - Multiple Transaction Allowed
#https://www.geeksforgeeks.org/dsa/stock-buy-sell/
def multi_buy(arr):
    n=len(arr)
    minSoFar=arr[0]
    profit=0
    tprofit=0
    for i in range(1,n):
      minSoFar=min(minSoFar,arr[i])
      profit=max(profit,arr[i]-minSoFar)
      if arr[i]<arr[i-1] :
         tprofit+=profit
         minSoFar=arr[i]
         profit=0
    tprofit+=profit
    return tprofit
print(multi_buy([100, 180, 260, 310, 40, 535, 695]))

#or 
def multi_buy(arr):
    n=len(arr)
    profit=0
    for i in range(1,n):
      if arr[i]>arr[i-1] :
         profit+=arr[i]-arr[i-1]
    return profit
print(multi_buy([100, 180, 260, 310, 40, 535, 695]))



    
        