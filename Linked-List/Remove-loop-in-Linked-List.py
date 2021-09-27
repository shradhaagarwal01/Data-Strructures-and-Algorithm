def removeLoop(head):
    if head is None or head.next is None:
        return
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            break
    if slow!=fast:
        return 
    if fast==head:
        while(fast.next!=head):
            fast = fast.next
        fast.next = None
        return
    else:
        slow = head
        while(slow.next!=fast.next):
            slow = slow.next
            fast = fast.next
        fast.next = None
        return 