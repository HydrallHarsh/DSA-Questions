class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                if len(stack) >= 2:
                    op1 = int(stack.pop())
                    op2 = int(stack.pop())
                    if token == '+':
                        stack.append(op2 + op1)
                    elif token == '-':
                        stack.append(op2 - op1)
                    elif token == '*':
                        stack.append(op2 * op1)
                    else:
                        stack.append(int(op2 / op1))
            # print(stack)
        return int(stack[-1])

