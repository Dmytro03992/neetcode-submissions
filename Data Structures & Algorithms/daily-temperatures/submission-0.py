class Solution:
        def dailyTemperatures(self, temps: list[int]) -> list[int]:
            n = len(temps)
            stack = []
            res = [0] * n
            for m in range(n):
                while stack and temps[m] > temps[stack[-1]]:
                    res[stack[-1]] = m - stack[-1]
                    stack.pop()
                stack.append(m)
            return res