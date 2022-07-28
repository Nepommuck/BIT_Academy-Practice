class Node:
    def __init__(self, value = 0, next = None) -> None:
        self.val = value
        self.next = next


def sort_list(first):
    guard = Node()
    guard.next = first

    akt = guard

    while akt.next is not None:
        mn = akt
        p = akt.next

        while p.next is not None:
            if p.next.val < mn.next.val:
                mn = p
            p = p.next
        p = mn
        mn = mn.next
        p.next = mn.next

        mn.next = akt.next
        akt.next = mn

        akt = akt.next
    
    return guard.next
