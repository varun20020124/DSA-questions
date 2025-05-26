from collections import deque
class Solution:
    def countComponents(self, n, edges):
        def bfs(i,visited,adj):
            visited[i] = True
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if visited[neighbor] == False:
                        visited[neighbor] = True
                        q.append(neighbor)
                        
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = [False] * n
        count = 0
        for i in range(n):
            if visited[i] == False:
                bfs(i,visited,adj)
                count += 1
        return count