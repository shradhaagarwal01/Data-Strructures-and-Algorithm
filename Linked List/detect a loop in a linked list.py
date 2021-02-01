def detectLoop(head):
    if head is None:
        return False
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast==slow:
            return True
    return False