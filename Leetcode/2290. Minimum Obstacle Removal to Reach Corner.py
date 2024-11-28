class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        min_heap = [(0,0,0)] #cost, row, col
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)

            if (x,y) == (m-1, n-1):
                return cost
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heapq.heappush(min_heap, (new_cost, nx, ny))
        return dist[m-1][n-1]
