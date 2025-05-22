class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = Node()
        curr = dummy
        while l1 or l2:
            total = carry
            if l1: total += l1.val 
            if l2: total += l2.val
            node = Node(total%10)
            carry = total//10
            curr.next = node
            curr = curr.next 
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        if carry>0:
            node = Node(carry)
            curr.next = node
        return dummy.next