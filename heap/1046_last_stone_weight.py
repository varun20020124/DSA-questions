import heapq
class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]
        max_heap = stones
        heapq.heapify(max_heap)
        while len(max_heap)>1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if x!=y:
                heapq.heappush(max_heap,x-y)
        if max_heap:
            return -heapq.heappop(max_heap)
        return 0