class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        size = len(s)
        a = {}
        b = {}

        for i in range(0, size):
            a[s[i]] = 0
            b[t[i]] = 0

        for i in range(0, size):
            a[s[i]] += 1
            b[t[i]] += 1
        
        if a == b:
            return True
        return False