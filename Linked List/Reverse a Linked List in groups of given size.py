def reverseList(head):
    # Code here
    if head is None or head.next is None:
        return head
    rest = reverseList(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return rest
    
def reverse(head, k):
    # Code here
    curr = head
    next = None
    prev = None
    count = 0
    while curr is not None and count!=k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count = count+1
        
    if next is not None:
        head.next = reverse(next,k)
    
    return prev