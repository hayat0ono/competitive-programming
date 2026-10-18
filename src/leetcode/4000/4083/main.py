class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        now = [0, 0]
        visited[0][0] = True
        while True:
            if grid[now[0]][now[1]] == 'R':
                nxt = [now[0], now[1] + 1]
            elif grid[now[0]][now[1]] == 'D':
                nxt = [now[0] + 1, now[1]]
            elif grid[now[0]][now[1]] == 'L':
                nxt = [now[0], now[1] - 1]
            elif grid[now[0]][now[1]] == 'U':
                nxt = [now[0] - 1, now[1]]
            if nxt[0] < 0 or nxt[0] >= n or nxt[1] < 0 or nxt[1] >= m:
                return now
            elif visited[nxt[0]][nxt[1]]:
                return now
            else:
                now = nxt
                visited[nxt[0]][nxt[1]] = True
