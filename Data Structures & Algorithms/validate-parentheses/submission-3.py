class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False 

        from collections import deque

        dic = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = deque()

        for i in s:
            if i in dic:
                top = stack.pop() if stack else "!"
                if dic[i] != top:
                    return False
                
            else:
                stack.append(i)
        
        return not stack

        