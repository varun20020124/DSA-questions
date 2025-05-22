class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists):
        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val, i, node))
        
        dummy = Node()
        curr = dummy

        while minheap:
            val, index, node = heapq.heappop(minheap)
            curr.next = Node(val)
            curr = curr.next

            if node.next:
                heapq.heappush(minheap, (node.next.val, index, node.next))
        
        return dummy.next