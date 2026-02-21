#https://neetcode.io/problems/two-integer-sum/question
#sol1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]
        return []

#sol2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
                seen[nums[i]]=i

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in seen:
                if i!=seen[diff]:
                    return [i,seen[diff]]


#sol3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i,num in enumerate(nums):
            a.append([num,i])
        a.sort()
        left,right=0,len(nums)-1
        while left<right:
            sum=a[left][0]+a[right][0]
            if sum==target:
                return [min(a[left][1],a[right][1]),max(a[left][1],a[right][1])]
            elif sum<target:
                left+=1
            else:
                right-=1
        