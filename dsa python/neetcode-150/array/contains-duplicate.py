#brute force , time complexity O(n^2) and space complexity O(1)
from ast import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True      
        return False

#using set, time complexity O(n) and space complexity O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

#using sorting, time complexity O(nlogn) and space complexity O(1)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False