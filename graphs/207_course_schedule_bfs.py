from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        def topological(adj):
            indegree = [0]*numCourses
            for i in range(len(adj)):
                for j in adj[i]:
                    indegree[j] += 1
            q = deque()
            for i in range(len(indegree)):
                if indegree[i]==0:
                    q.append(i)
            topo = []
            while q:
                node = q.popleft()
                topo.append(node)
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            return topo
        adj = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
        return len(topological(adj))==numCourses