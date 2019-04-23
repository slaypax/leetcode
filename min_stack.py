# still doesn't pass all test cases. 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minElement = 0
        

    def push(self, x: int) -> None:
        if len(self.items) == 0:
            self.minElement = x
            self.items.append(x)
        
        if len(self.items) > 0:
            if x >= self.minElement:
                self.items.append(x)
            if x < self.minElement:
                self.items.append(2 * x - self.minElement)
                self.minElement = x

    def pop(self) -> None:
        element = self.items.pop()
        if element < self.minElement:
            self.minElement = (2 * self.minElement) - element
        return element
    

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minElement