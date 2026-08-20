class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini.append(val)
        else:
            if val <= self.mini[-1]:
                self.mini.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        out = self.stack.pop()
        if self.mini[-1] == out:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]
        
