from collections import deque
class Tree():
    def __init__(self, data=0, left=None, right=None, parent= None):
        self.size = 0
        self.data = data
        self.left = left
        if left:
            self.left.parent = self
        self.right = right
        self.parent = parent
        if self.right:
            self.size += 1
        if self.left:
            self.size +=1
        if self.parent:
            self.parent.size += self.size
    def __str__(self):
        return self.data

def test_tree_height_balanced(root):
    def helper(root, h):
        if not root:
            return h
        left_height = helper(root.left, h+1)
        right_height = helper(root.right, h+1)
        if left_height == -1 or right_height == -1:
            return -1
        if left_height - right_height > 1:
            return -1
        return max(left_height, right_height)
    height = helper(root, 1)
    if height >= 0:
        return True
    return False

def is_tree_symmetric(right, left):
    if not right and not left:
        return True
    elif right and left and right.data == left.data:
        return is_tree_symmetric(right.right, left.left) and is_tree_symmetric(right.left, left.right)
    return False

def sum_root_to_leaf(root, num):
    if not root:
        return 0
        return num
    #print 'num', num
    num = num <<1 | root.data
    #print 'new num', num
    if not root.right and not root.left:
        return num
    return sum_root_to_leaf(root.left, num) + sum_root_to_leaf(root.right, num)

def root_to_leaf_path(root, n):
    n -= root.data

    if n == 0:
        if not root.right and not root.left:
            return True
        return False
    elif n > 0:
        left = right = False
        if root.left:
            left = root_to_leaf_path(root.left, n)
        if root.right:
            right = root_to_leaf_path(root.right, n)
        return right or left
    else:
        return False

def inorder_traversal(root):
    s, l = [], []
    while s or root:
        if root:
            s.append(root)
            root = root.left
        else:
            node = s.pop()
            print node.data
            root = node.right
def compute_kth_node(root, k):
    if k == 1:
        return root
    else:
        if root.left and k < root.left.size:
            return compute_kth_node(root.left, k)
        elif k - root.left.size == 1:
            return root
        else:
            k = k-1
            if root.left:
                k -= root.left.size
            return compute_kth_node(root.right)
    
def find_successor(head):
    if head.right:
        new_head = head.right
        while new_head.left:
            new_head = new_head.left
        return new_head
    elif head == head.parent.left:
        return head.parent
    elif head == head.parent.right:
        new_head = head
        while new_head == head.parent.right:
            new_head = new_head.parent
        if not new_head.parent:
            return None
        return head.parent



if __name__ == '__main__':
    head = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5))
    print test_tree_height_balanced(head)
    head = Tree(1, Tree(2, right=Tree(3)), Tree(2,left=Tree(3)))
    print is_tree_symmetric(head.right, head.left)
    head = Tree(1,Tree(0,Tree(0,Tree(0),Tree(1)),Tree(1,right=Tree(1,Tree(0)))),
                Tree(1,Tree(0,right=Tree(0,Tree(1,right=Tree(1)),Tree(0))),Tree(0,right=Tree(0))))
    print 'head size', head.size
    head = Tree(1,Tree(0,Tree(0),Tree(1)))
    print sum_root_to_leaf(head,0)
    head = Tree(1, Tree(2, Tree(5), Tree(6)))
    assert root_to_leaf_path(head, 8) == True
    assert root_to_leaf_path(head, 9) == True
    assert root_to_leaf_path(head, 5) == False
    print 'printing'
    inorder_traversal(head)
    head = Tree('a', Tree('b', Tree('d'), Tree('e', Tree('f',Tree('g')),Tree('h'))),
                Tree('c', Tree('i'), Tree('j', right=Tree('k'))))
    assert find_successor(head).data == 'i'
    assert find_successor(head.left.right.left.left).data == 'f'