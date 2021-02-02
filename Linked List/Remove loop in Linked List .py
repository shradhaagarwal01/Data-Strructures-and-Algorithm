def removeLoop(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            break
    if slow!=fast:
        return 
    slow = head
    while(slow.next!=fast.next):
        slow = slow.next
        fast = fast.next
    fast.next = None