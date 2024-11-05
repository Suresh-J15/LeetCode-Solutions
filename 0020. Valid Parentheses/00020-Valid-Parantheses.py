class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in '[({':
                stack.append(bracket)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped == '[' and bracket != ']':
                    return False
                elif popped == '(' and bracket != ')':
                    return False
                elif popped == '{' and bracket != '}':
                    return False
                else:
                    continue
        
        return True if not stack else False