class Solution {
public:
    int trap(vector<int>& h) {
        int l = 0;
        int r = h.size() - 1;
        int maxl = 0;
        int maxr = 0;
        int res = 0;
        while (l < r) {
            maxl = max(maxl, h[l]);
            maxr = max(maxr, h[r]);
            res += (maxl > 0) ? maxl : 0;
            res -= h[l];
            res += (maxr > 0) ? maxr : 0;
            res -= h[r];
            if (h[l] <= h[r]) l += 1;
            else if (h[l] >= h[r]) r -= 1;
        }
        return res;
    }
};
