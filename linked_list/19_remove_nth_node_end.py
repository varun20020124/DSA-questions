class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next

        if length == n:
            return head.next
        
        curr, prev = head, None
        for _ in range(length - n):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        return head