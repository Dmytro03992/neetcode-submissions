#include<unordered_map>
#include<string>
#include<algorithm>

using namespace std;

class Solution {
public:
    unsigned short int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> h;
        int c = 0, maxc = 0, l = 0, r = 0;
        while (r < s.size()) {
            if (h.empty() || h[s[r]] < 1) { ++h[s[r]]; ++r; }
            else { --h[s[l]]; ++l; }
            c = r - l;
            maxc = max(maxc, c);
        }     
        return maxc;
    }
};