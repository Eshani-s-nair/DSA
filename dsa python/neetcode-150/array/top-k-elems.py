#https://neetcode.io/problems/top-k-elements-in-list/history?submissionIndex=2

#sol1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        arr=[]
        for num,cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
    
    
#sol2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        heap=[]
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        
        


            
        
       


        
            
        