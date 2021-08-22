class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [float('inf')]
        # self.maxStack = [-float('inf')]
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1]))
        # self.maxStack.append(max(val, self.maxStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # self.maxStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
