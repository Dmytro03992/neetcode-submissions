class Solution:
    def twoSum(self, nums: List[int], target: int):
        a = {}
        indexes = [0, 0]

        for i in range(0, len(nums)):
            a[nums[i]] = i

        for i in range(0, len(nums)):
            if a.get(target-nums[i]) != None and a[target-nums[i]] != i:
                if nums[i] + nums[a[target - nums[i]]] == target:
                    indexes[0] = i
                    indexes[1] = a[target-nums[i]]
                    return indexes
        return None
                