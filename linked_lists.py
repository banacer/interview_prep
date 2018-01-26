
class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def convert_to_linked_list(l):
    head = Node(l[0])
    walker = head
    for num in l[1:]:
        walker.next = Node(num)
        walker = walker.next
    return head
def print_linked_list(l):
    walker = l
    while walker:
        print walker.data, ' ',
        walker = walker.next
    print ''

def merge_two_lists(l1,l2):
    w1 = l1
    w2 = l2
    head = Node(-1)
    current = head
    while w1 and w2:
        if w1.data < w2.data:
            current.next = w1
            w1 = w1.next
        else:
            current.next = w2
            w2 = w2.next
        current = current.next
    if w1:
        current.next = w1
    elif w2:
        current.next = w2

    return head.next

def reverse_linked_list(l):
    if not l:
        return l
    current = l
    next = l.next
    current.next = None
    while next:
        new_next = next.next
        next.next = current
        current = next
        next = new_next
    return current

def reverse_sublist(l, s, f):
    walker = l
    for _ in range(1,s-1):
        walker = walker.next
    head = walker.next

def test_for_cyclicity(l):
    slow = l.next
    fast = l.next.next
    while slow and fast:
        if slow.data == fast.data:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
if __name__ == '__main__':
    l1 = convert_to_linked_list([i for i in range(0,10,2)])
    l2 = convert_to_linked_list([i for i in range(1, 11, 2)])

    print_linked_list(l1)
    print_linked_list(l2)
    print_linked_list(merge_two_lists(l1,l2))
    l = reverse_linked_list(l1)
    print_linked_list(l)
    assert test_for_cyclicity(l) ==  False