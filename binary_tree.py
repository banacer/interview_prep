class Tree():
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
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

if __name__ == '__main__':
    head = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5))
    print test_tree_height_balanced(head)
    head = Tree(1, Tree(2, right=Tree(3)), Tree(2,left=Tree(3)))
    print is_tree_symmetric(head.right, head.left)