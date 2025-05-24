from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        hashmap = {}
        q = deque()
        q.append(node)
        while q:
            x = q.popleft()
            if x not in hashmap:
                hashmap[x] = Node(x.val)
            for adj in x.neighbors:
                if adj not in hashmap:
                    hashmap[adj] = Node(adj.val)
                    q.append(adj)
                hashmap[x].neighbors.append(hashmap[adj])
        return hashmap[node]
