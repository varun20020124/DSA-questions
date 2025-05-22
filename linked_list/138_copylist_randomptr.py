class Node:
    def __init__(self, val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head):
        hashmap = {None:None}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        for key,val in hashmap.items():
            if key:
                val.next = hashmap[key.next]
                val.random = hashmap[key.random]
        return hashmap[head]
         