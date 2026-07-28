class MinStack:

    def __init__(self):

        self.stack = [] # full stack with values in "same order"
        self.Minstack = [] # minstack
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.Minstack:
            self.Minstack.append(val)
        else:
            self.Minstack.append(min(val, self.Minstack[-1]))
        

    def pop(self) -> None:
        self.Minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:

        return self.Minstack[-1]
        
