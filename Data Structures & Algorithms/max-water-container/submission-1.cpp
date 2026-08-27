class Solution {
public:
    int maxArea(vector<int>& heights) {
        unsigned int l = 0;
        unsigned int r = heights.size() - 1;
        unsigned int m = 0;
        while (l < r) {
            m = max(m, min(heights[l], heights[r]) * (r - l) );
            if (heights[l] >= heights[r])
                r -= 1;
            else if (heights[l] <= heights[r])
                l += 1;
        }
        return m;
    }
};
