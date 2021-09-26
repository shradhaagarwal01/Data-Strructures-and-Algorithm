def removeDuplicates(head):
    if head is None or head.next is None:
        return
    curr = head
    next = head.next
    while(curr.next is not None):
        if curr.data == next.data:
            curr.next = next.next
            next = next.next
        else:
            curr = curr.next
            next = next.next