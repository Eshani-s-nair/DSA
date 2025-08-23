// Problem: 287. Find the Duplicate Number
// Link: https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                return nums[i];
            }
        }
        return 0;
    }
}