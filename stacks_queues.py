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

def compute_rpn_expression(s):
    data = s.split(',')
    s = []
    for op in data:
        if op.isdigit():
            s.append(op)
        else:
            a = s.pop()
            b = s.pop()
            c = compute(int(a), int(b), op)
            s.append(c)
    return s.pop()
def compute(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        return None
def parenthesis_checker(expr):
    s = []
    for c in expr:
        if c in '([{':
            s.append(c)
        elif c in ')]}':
            match = s.pop()
            if (c == ')' and match != '(' )or (c == ']' and match != '[') or (c == '}' and match != '{'):
                return False
        else:
            return False
    return True

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
    assert compute_rpn_expression('5,3,+') == 8
    assert compute_rpn_expression('3,4,+,2,*,1,+') == 15
    assert parenthesis_checker('()()') ==  True
    assert parenthesis_checker('[}') == False
