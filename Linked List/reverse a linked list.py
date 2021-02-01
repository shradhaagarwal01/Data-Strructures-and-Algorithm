# resursive
def reverseList(head):
    # Code here
    if head is None or head.next is None:
        return head
    rest = reverseList(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return rest


#iterative
def reverseList(head):
    # Code here
    prev = None
    next = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next      
    return prev
        