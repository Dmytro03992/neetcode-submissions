class Solution {
public:
    int trap(vector<int>& h) {
        int l = 0, maxr = 0, maxl = 0, res = 0;
        int r = h.size() - 1;
        while (l < r) {
            maxl = max(maxl, h[l]);
            maxr = max(maxr, h[r]);
            res = res + ((maxl > 0) ? maxl : 0) - h[l] + ((maxr > 0) ? maxr : 0) - h[r];
            if (h[l] <= h[r]) l += 1;
            else if (h[l] >= h[r]) r -= 1;
        }
        return res;
    }
};
