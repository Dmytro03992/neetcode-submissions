class Solution:
    def maxArea(self, h: list[int]) -> int:

        l: int = 0
        r: int = len(h)-1
        max_area: int = 0
        
        while l < r:
            current_area = (r - l) * (min(h[l], h[r]))
            max_area = max(max_area, current_area)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return max_area