class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        special = []

        for i in range(0, len(s)):
            if s[i].isalpha() or s[i].isdigit():
                special.append(s[i])

        if special == special[::-1]:
            return True
        return False