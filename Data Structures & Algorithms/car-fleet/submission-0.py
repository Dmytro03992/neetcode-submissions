class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        pair = [[position[i], speed[i]] for i in range(len(position))]
        for i in sorted(pair)[::-1]:
            t: float = (target - i[0]) / i[1]
            stack.append(t)
            
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)