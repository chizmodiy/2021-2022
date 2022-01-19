class Stack:
    def __init__(self):
        self.items = []
        self._LastValueNum = None

    def showStack(self):
        return self.items

    def push(self, item):
        if isinstance(item, int):
            self.items.append(item)
            self._LastValueNum = item

        else:
            raise ValueError('Enter an integer')

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            self._LastValueNum = self.items.index(self._LastValueNum - 1)
            return self.items.pop()

    def SumOfElement(self):
        return sum(self.items)


new = Stack()
new.push(3)
new.push(2)
new.push(4)
new.push(5)
new.push(6)
print(new.showStack())
new.pop()
print(new.showStack())
print(new.SumOfElement())
print(dir(new))
