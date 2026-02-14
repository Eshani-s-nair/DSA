#Stock Buy and Sell - Max one Transaction Allowed
#https://www.geeksforgeeks.org/dsa/best-time-to-buy-and-sell-stock/
def buy_sell(arr):
    profit=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[j]-arr[i])>profit:
                profit=arr[j]-arr[i]
    return profit

print(buy_sell( [7, 10, 1, 3, 6, 9, 2]))


#or

def buy_sell(arr):
    minSoFar=arr[0]
    profit=0
    for i in range(1,len(arr)):
        minSoFar=min(minSoFar,arr[i])
        profit=max(profit,arr[i]-minSoFar)
    return profit
print(buy_sell([1, 3, 6, 9, 11]))