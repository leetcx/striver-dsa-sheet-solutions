class MyStack:

    def __init__(self):
        self.q=deque()
       

    def push(self, x: int) -> None:
        self.q.append(x)
        n=len(self.q)

        for i in range (n-1):
            item=self.q.popleft()
            self.q.append(item)


    def pop(self) -> int:
        x=self.q.popleft()
        return x
    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()