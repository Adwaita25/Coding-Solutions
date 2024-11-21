class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for val in walls:
            grid[val[0]][val[1]] = 2
        
        for val in guards:
            grid[val[0]][val[1]] = 3

        for val in guards:
            row, col = val[0], val[1]

            for i in range(row + 1, m):
                if grid[i][col] in (2,3):
                    break
                grid[i][col] = 1
            
            for i in range(row - 1, -1, -1):
                if grid[i][col] in (2,3):
                    break
                grid[i][col] = 1

            for i in range(col + 1, n):
                if grid[row][i] in (2, 3):
                    break
                grid[row][i] = 1
            
            for i in range(col - 1, -1, -1):
                if grid[row][i] in (2,3):
                    break
                grid[row][i] = 1
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
        return count
