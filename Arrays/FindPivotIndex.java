// Problem: 724. Find Pivot Index
// Link: https://leetcode.com/problems/find-pivot-index/description/
class Solution {
    public int pivotIndex(int[] nums) {
        int totalSum = 0;
        for (int n : nums) {
            totalSum += n;
        }

        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int rightSum = totalSum - leftSum - nums[i];
            if (leftSum == rightSum) {
                return i;
            }
            leftSum += nums[i];
        }

        return -1;
    }
}
