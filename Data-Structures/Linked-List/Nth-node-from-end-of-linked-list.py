def getNthFromLast(head,n):
    #code here
    if head is None:
        return -1
    p1 = head
    p2 = head
    c = 0
    while c!=n:
        if p1 is None:
            return -1
        p1 = p1.next
        c =c+1
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2.data