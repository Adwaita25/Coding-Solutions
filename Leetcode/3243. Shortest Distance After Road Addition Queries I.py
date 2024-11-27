class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]

        def path():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))

            while q:
                curr, length = q.popleft()
                if curr == n-1:
                    return length
                for i in adj[curr]:
                    if i not in visit:
                        q.append((i, length+1))
                        visit.add(i)
        res = []
        for src, dist in queries:
            adj[src].append(dist)
            res.append(path())
        return res
