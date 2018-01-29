from collections import namedtuple
class Stack:
    Node = namedtuple('Node',('element', 'max'))
    def __init__(self):
        self._l = []

    def empty(self):
        return not self._l

    def max(self):
        if not self.empty():
            return self._l[-1].max

    def pop(self):
        return self._l.pop().element

    def push(self, x):
        if self.empty():
            n = Stack.Node(x,x)
        else:
            if self._l[-1].element < x:
                max = x
            else:
                max = self._l[-1].element
            n = Stack.Node(x, max)
        self._l.append(n)

if __name__ == '__main__':
    s = Stack()
    assert s.empty() == True
    s.push(1)
    assert s.max() == 1
    s.push(3)
    assert s.max() == 3
    s.push(2)
    assert s.max() == 3
    s.push(5)
    assert s.max() == 5
    assert s.pop() == 5
    assert s.max() == 3
