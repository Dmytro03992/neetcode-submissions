class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 1;
        int r = nums.size();
        while (l < r) {
            if (nums[l-1] + nums[r-1] < target) 
                l += 1;
            else if (nums[l-1] + nums[r-1] > target) 
                r -= 1;
            else 
                return {l, r};
        }
        return {0, 0};
    }
};
