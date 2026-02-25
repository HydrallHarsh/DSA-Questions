class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_ele = float('inf')

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or min_val > val:
            min_val = val
        self.stack.append([val,min_val])       
        # self.min_ele = min(self.min_ele, val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) != 0 else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) != 0 else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()