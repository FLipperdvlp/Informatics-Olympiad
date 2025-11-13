import sys
input = sys.stdin.readline

n, k = map(int, input().split())
start_board = [list(map(int, input().split())) for _ in range(n)]
target_board = [list(map(int, input().split())) for _ in range(n)]

start_pos = [None] * (k + 1)
target_pos = [None] * (k + 1)

for i in range(n):
    for j in range(n):
        val = start_board[i][j]
        if val:
            start_pos[val] = (i, j)
        val = target_board[i][j]
        if val:
            target_pos[val] = (i, j)

moves = []
occupied = set(start_pos[1:])

dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)]

def is_safe(x, y, occ):
    if not (0 <= x < n and 0 <= y < n):
        return False
    for dx, dy in dirs:
        if (x + dx, y + dy) in occ:
            return False
    return True

def move(king, x, y):
    moves.append((king, x + 1, y + 1))
    occupied.remove(pos[king])
    pos[king] = (x, y)
    occupied.add((x, y))

def go_to(king, tx, ty):
    x, y = pos[king]
    while x != tx or y != ty:
        best = None
        min_dist = abs(x - tx) + abs(y - ty)
        occ = occupied
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if is_safe(nx, ny, occ - {(x, y)}):
                dist = abs(nx - tx) + abs(ny - ty)
                if dist < min_dist:
                    min_dist = dist
                    best = (nx, ny)
        if best:
            move(king, best[0], best[1])
            x, y = best
        else:
            break

grid = [(i, j) for i in range(0, n, 3) for j in range(0, n, 3)]

if len(grid) < k:
    print("NIE")
    sys.exit(0)

pos = start_pos[:]
for king in range(1, k + 1):
    go_to(king, *grid[king - 1])

for king in range(1, k + 1):
    go_to(king, *target_pos[king])

print("TAK")
print(len(moves))
for m in moves:
    print(*m)
