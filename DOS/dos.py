from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
changes = [tuple(map(int, input().split())) for _ in range(q)]

dist = [[-1] * n for _ in range(n)]
queue = deque()
queue.append((0, 0))
dist[0][0] = 0

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    x, y = queue.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

forts = set()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'F':
            forts.add((i, j))

def min_turns(forts):
    dists = [dist[x][y] for x, y in forts]
    dists.sort()
    return max(d + i for i, d in enumerate(dists)) if dists else 0

results = []
results.append(min_turns(forts))

for x, y in changes:
    x -= 1
    y -= 1
    if (x, y) in forts:
        forts.remove((x, y))
    else:
        forts.add((x, y))
    results.append(min_turns(forts))

for r in results:
    print(r)
