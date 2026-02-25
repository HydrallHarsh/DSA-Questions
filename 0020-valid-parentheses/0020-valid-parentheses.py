class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_modified = False
        pairs = {'}' : '{', ')' : '(', ']':'['}
        for char in s:
            # if char in pairs.values():
            #     stack.append(char)
            #     stack_modified = True
            if char in pairs and stack and stack[-1] == pairs[char]:
                stack.pop()
                continue 
            stack.append(char)
        return len(stack) == 0