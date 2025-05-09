import heapq
class Solution:
    def kClosest(self, points, k):
        def distance(point):
            return (point[0])**2 + (point[1])**2
        min_heap = []
        heapq.heapify(min_heap)
        for point in points:
            heapq.heappush(min_heap, (distance(point), point))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res 