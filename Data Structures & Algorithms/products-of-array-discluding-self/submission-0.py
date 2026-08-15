class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: list[int] = [1] * len(nums)
        prefix = 1
        postfix = 1
        i = 0

        while i < len(nums):
            res[i] *= prefix
            prefix *= nums[i]
            i += 1
            
        i -= 1
        while i >= 0:
            res[i] *= postfix
            postfix *= nums[i]
            i -= 1

        return res