class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        res: list[list[int]] = []
        n.sort()
        seen = set()
        for i in range(len(n)):
            if n[i] not in seen:
                l = i + 1
                r = len(n)-1
                while l < r:
                    sum = n[l] + n[r]
                    if sum + n[i] > 0:
                        r -= 1
                    elif sum + n[i] < 0:
                        l += 1
                    else:
                        res.append([n[i], n[l], n[r]])
                        l += 1
                        r -= 1
                        while n[l] == n[l - 1] and l < r:
                            l += 1
            else:
                continue
            seen.add(n[i])
        
        return res