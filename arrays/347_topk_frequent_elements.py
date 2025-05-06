import heapq
class Solution:
    def topkFrequent(self, nums, k):
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        max_heap  = []
        for key,val in frequency.items():
            max_heap.append((-val,key))
        heapq.heapify(max_heap)
        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(max_heap)[1])
        return top_k