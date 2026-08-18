class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        res = 0
        while l < r:
            if height[l] >= height[r]:
                maxR = max(maxR, height[r])
                r -= 1
                if maxR - height[r] >= 0:
                    res += maxR - height[r]
            elif height[l] <= height[r]:
                maxL = max(maxL, height[l])
                l += 1
                if maxL - height[l] >= 0:
                    res += maxL - height[l]
        return res
        