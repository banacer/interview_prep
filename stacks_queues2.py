from collections import deque

class Tree():
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return self.data

def find_nodes_in_level(head):
    parent = deque()
    children = deque()
    parent.append(head)
    l = []
    l_sub = []
    while parent:
        while parent:
            node = parent.popleft()
            if node:
                l_sub.append(node.data)
                children.append(node.right)
                children.append(node.left)
        l.append(l_sub)
        l_sub = []
        parent = children
        children = deque()
    return l

if __name__== '__main__':
    head = Tree(1,Tree(2,Tree(3),Tree(4)),Tree(5,Tree(6),Tree(7)))
    l = find_nodes_in_level(head)
    print(l)
