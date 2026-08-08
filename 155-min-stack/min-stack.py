class MinStack:

    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self, value: int) -> None:
        
        self.st1.append(value)
        if not self.st2 or self.st2[-1]>=value:
            self.st2.append(value)
        



    def pop(self) -> None:
        pv=self.st1.pop()
        if pv==self.st2[-1]:
            self.st2.pop()
    def top(self) -> int:
        return self.st1[-1]

    def getMin(self) -> int:
        return self.st2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()