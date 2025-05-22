class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        # Find the middle of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second list
        second = slow.next
        prev = None
        slow.next = prev
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # combine the two lists
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
