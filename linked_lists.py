
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
def length(l):
    if not l:
        return 0
    size = 0
    walker = l
    while walker:
        size +=1
        walker = walker.next
    return size

def test_for_cyclicity(l):
    slow = l.next
    fast = l.next.next
    while slow and fast:
        if slow.data == fast.data:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

def test_overlapping(l1, l2):
    len1 = length(l1)
    len2 = length(l2)
    if len1 > len2:
        for _ in range(len1-len2):
            l1 = l1.next
    else:
        for _ in range(len2-len1):
            l2 = l2.next
    while l1 and l2:
        if l1.data == l2.data:
            return True
        l1 = l1.next
        l2 = l2.next
    return False
def delete_kth_element(l,k):
    w1 = l
    w2 = l
    for _ in range(k+1):
        w2 = w2.next
    while w2:
        w1 = w1.next
        w2 = w2.next
    w1.next = w1.next.next
    return l

def remove_duplicates(l):
    w = l
    key = w.data
    node = w
    while w.next:
        w = w.next
        if w.data == key:
            continue
        key = w.data
        node.next = w
        node = w
    node.next = None
    return l


if __name__ == '__main__':
    l1 = convert_to_linked_list([i for i in range(0,10,2)])
    l2 = convert_to_linked_list([i for i in range(1, 11, 2)])

    print_linked_list(l1)
    print_linked_list(l2)
    print_linked_list(merge_two_lists(l1,l2))
    l = reverse_linked_list(l1)
    print_linked_list(l)
    assert test_for_cyclicity(l) == False
    deleted = delete_kth_element(l,7)
    print_linked_list(deleted)
    l3 = convert_to_linked_list([1,1,2,2,4,5,6,7,7,7,7])
    res = remove_duplicates(l3)
    print_linked_list(l3)