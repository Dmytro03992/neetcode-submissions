class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 1 # left pointer
        r = len(nums)  # right pointer

        while l < r:
            if nums[l-1] + nums[r-1] < target:
                l += 1
            elif nums[l-1] + nums[r-1] > target:
                r -= 1
            else:
                return [l, r]
        return [-1, -1]