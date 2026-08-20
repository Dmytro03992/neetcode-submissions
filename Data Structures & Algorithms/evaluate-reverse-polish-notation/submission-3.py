import operator as o
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
        '+': o.add,
        '-': o.sub,
        '*': o.mul,
        '/': lambda a, b: int(a / b)
        }
        for i in tokens:
            if i in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(ops[i](num2, num1))
            else:
                stack.append(int(i))
        return stack.pop()