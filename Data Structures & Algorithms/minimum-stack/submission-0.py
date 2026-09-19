class MinStack:

    def __init__(self):
        self.stack = []
        self.prest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prest:
            self.prest.append(min(val, self.prest[-1]))
        else:
            self.prest.append(val)

    def pop(self) -> None:
        self.prest.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prest[-1]
