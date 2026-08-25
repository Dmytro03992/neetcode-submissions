#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;

        for (int i = 0; i < nums.size(); ++i)
            hash[nums[i]] = i;

        for (int i = 0; i < nums.size(); ++i) {
            if (hash.count(target - nums[i]))
                if (nums[i] + nums[hash[target-nums[i]]] == target && hash[target - nums[i]] != i) 
                    return {i, hash[target - nums[i]]};
        
        }
        
        return {-1, -1};
    };
};