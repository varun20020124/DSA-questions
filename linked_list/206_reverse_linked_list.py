class Node:
    def __init__(self,val = 0,next = None):
        self.val = None
        self.next = None
class Solution:
    def reverseList(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
