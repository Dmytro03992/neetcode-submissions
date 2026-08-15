class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        elif len(arr) == 0:
            return 0

        nums = set()
        longest: int = 0

        for i in arr:
            nums.add(i)
            
        for i in arr:
            if i - 1 not in nums:
                length: int = 0
                while (i + length) in nums:
                    length += 1
                longest = max(longest, length)

        return longest