class Solution:
    def isValid(self, s: str):
	
        sample = {')': '(','}': '{',']': '['}
        stack = deque()
	
        for i in s:
        
            if i in sample.values():
                stack.appendleft(i)
            
            if i in sample:
                if stack and stack[0] == sample[i]:
                    stack.popleft()
                else:
                    return False
            else:
                continue
		
        return not stack