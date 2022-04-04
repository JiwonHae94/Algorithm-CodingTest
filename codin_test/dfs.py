
#https://www.acmicpc.net/problem/1260
from collections import deque
def solve1260():
    N, M, V = map(int, input().split())
    matrix = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(int(M)):
        fr, to = map(int, input().split())
        matrix[fr][to] = matrix[to][fr] = 1


    dfs_visited = [0 for _ in range(N + 1)]
    bfs_visited = [0 for _ in range(N + 1)]

    def dfs(V):
        dfs_visited[V] = 1
        print(V, end = " ")

        for i in range(1, N + 1):
            if dfs_visited[i] == 0 and matrix[V][i] == 1:
                dfs(i)

    def bfs(V):
        queue = deque()
        queue.append(V)

        bfs_visited[V] = 1
        print(V, end =" ")

        while queue:
            V = queue.popleft()

            for i in range(1, N + 1):
                if bfs_visited[i] == 0 and matrix[V][i] == 1:
                    queue.append(i)
                    bfs_visited[i] = 1
                    print(i, end = " ")
    dfs(V)
    print()
    bfs(V)

#https://www.acmicpc.net/problem/2606
def solve2606():
    N = int(input())
    matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(int(input())):
        A, B = map(int, input().split())
        matrix[A][B] = matrix[B][A] = 1

    visited = [0 for _ in range(N + 1)]

    def dfs(V):
        num_infected = 1
        visited[V] = 1

        for i in range(1, N+1):
            if visited[i] == 0 and matrix[V][i] == 1:
                num_infected += dfs(i)

        return num_infected


    num_infected = dfs(1)
    print(num_infected - 1)

#https://www.acmicpc.net/problem/2667
def solve2667():
    n = int(input())
    matrix = []

    for i in range(n):
        matrix.append(list(input()))


    def dfs(x, y):
        matrix[y][x] = '0'
        size = 1

        mx = [1, -1, 0, 0]
        my = [0, 0, 1, -1]

        for i in range(4):
            new_x = x + mx[i]
            new_y = y + my[i]

            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n:
                if matrix[new_y][new_x] == '1':
                    size += dfs(new_x, new_y)

        return size

    num_island = 0
    islands = []

    for y in range(n):
        for x in range(n):
            if matrix[y][x] == '1':
                num_island += 1
                islands.append(dfs(x, y))

    print(num_island)
    for i in sorted(islands):
        print(i)

#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)

def solve1012():
    num_test = int(input())

    for i in range(num_test):
        M, N, C = map(int, input().split())
        matrix = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(C):
            A, B = map(int, input().split())
            matrix[B][A] = 1

        def dfs(x, y):
            matrix[y][x]= 0

            mx = [1, -1, 0, 0]
            my = [0, 0, 1, -1]

            for i in range(4):
                new_x = x + mx[i]
                new_y = y + my[i]

                if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                    if matrix[new_y][new_x] == 1:
                        dfs(new_x, new_y)

        num_bug = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                   num_bug += 1
                   dfs(j, i)
        print(num_bug)

#https://www.acmicpc.net/problem/2178
from collections import deque
import sys
def solve2178():
    M, N = map(int,  map(int, sys.stdin.readline().strip().split()))
    matrix = []

    for i in range(M):
        matrix.append(list(map(int, sys.stdin.readline().strip())))

    def dfs(x, y):
        queue = deque()
        queue.append([x, y])

        mx = [1, -1, 0, 0]
        my = [0, 0, 1, -1]

        while queue:
            cx, cy = queue.popleft()

            for i in range(4):
                new_x = cx + mx[i]
                new_y = cy + my[i]

                if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M:
                    if matrix[new_y][new_x] == 1:
                        matrix[new_y][new_x] = matrix[cy][cx] + 1
                        queue.append([new_x, new_y])

    dfs(0, 0)
    print(matrix[M-1][N-1])

# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
def solve7576():
    M, N =  map(int, sys.stdin.readline().strip().split())
    matrix = []
    dates = [[-1 for _ in range(M)] for _ in range(N)]
    riped = deque()

    for i in range(N):
        rows = list(map(int, sys.stdin.readline().strip().split()))
        matrix.append(rows)

        index = [[idx, i] for idx, value in enumerate(rows) if value == 1]
        riped += index

        for x, y in index:
            dates[y][x] = 0

    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    while riped:
        x, y = riped.popleft()

        for i in range(4):
            new_x = x + mx[i]
            new_y = y + my[i]

            if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                if matrix[new_y][new_x] == 0 and dates[new_y][new_x] == -1:
                    dates[new_y][new_x] = dates[y][x] + 1
                    riped.append([new_x, new_y])

    rslt = 0
    for i in range(N):
        for j in range(M):
            if dates[i][j] == -1 and matrix[i][j] == 0:
                print(-1)
                return
            rslt = max(rslt, dates[i][j])
    print(rslt)

#https://www.acmicpc.net/problem/7569
import sys
from collections import deque
def solve7569():
    M, N, H = map(int, sys.stdin.readline().split())
    mx = [1, -1, 0, 0, 0, 0]
    my = [0, 0, 1, -1, 0, 0]
    mz = [0, 0, 0, 0, 1, -1]

    graph = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

    matrix = deque()
    queue = deque()

    for h in range(H):
        temp = []
        for n in range(N):
            t = list(map(int, sys.stdin.readline().split()))
            temp.append(t)

            riped_tomatos = [[idx, n, h] for idx, _ in enumerate(t) if _ == 1]
            queue += riped_tomatos

            for x,y,z in riped_tomatos:
                graph[z][y][x] = 0

        matrix.append(temp)

    while queue:
        cx, cy, cz = queue.popleft()

        for i in range(6):
            new_x = cx + mx[i]
            new_y = cy + my[i]
            new_z = cz + mz[i]

            if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N and new_z >= 0 and new_z < H:
                if graph[new_z][new_y][new_x] == -1 and matrix[new_z][new_y][new_x] == 0:
                    graph[new_z][new_y][new_x] = graph[cz][cy][cx] + 1
                    queue.append([new_x, new_y, new_z])

    max_day = -1

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == -1 and matrix[z][y][x] == 0:
                    print(-1)
                    return
                else:
                    max_day = max(graph[z][y][x], max_day)

    print(max_day)

#https://www.acmicpc.net/problem/1697
import sys
from collections import deque
def solve1697():
    N, K = map(int, sys.stdin.readline().split())
    movement = [lambda x : x-1, lambda x : x+1, lambda x :x*2]
    secs = [0 for _ in range(100000 + 1)]
    queue = deque([N])
    current = N

    while current != K:
        l = queue.popleft()
        current = l

        for i in movement:
            nl = i(l)

            if 0 <= nl < 100000 + 1 and secs[nl] == 0:
                secs[nl] = secs[l] + 1
                queue.append(nl)

    print(secs[K])


#https://www.acmicpc.net/problem/2206
from collections import deque
def solve2206():
    N, M = map(int, sys.stdin.readline().split())
    distance = [[[0, 0] for _ in range(M)] for _ in range(N)]
    matrix = []
    distance[0][0][0] = 1

    for i in range(N):
        matrix.append(list(map(int, input())))

    queue = deque()
    queue.append([0, 0, 0])
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    while queue:
        x, y, flag = queue.pop()

        if x == M - 1 and y == N - 1:
            print(distance[y][x][flag])
            return

        for i in range(4):
            new_x = x + mx[i]
            new_y = y + my[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                if matrix[new_y][new_x] == 0 and distance[new_y][new_x][flag] == 0:
                    queue.append((new_x, new_y, flag))
                    distance[new_y][new_x][flag] = distance[y][x][flag] + 1
                elif matrix[new_y][new_x] == 1 and flag == 0:
                    queue.append((new_x, new_y, 1))
                    distance[new_y][new_x][1] = distance[new_y][new_x][flag] + 1

    print(-1)

# https://www.acmicpc.net/problem/7562
from collections import deque
def solve7562():
    N = int(input())
    dx = [+2, +1, -1, -2, -2, -1, +1, +2]
    dy = [+1, +2, +2, +1, -1, -2, -2, -1]

    for i in range(N):
        I = int(input())

        matrix = [[-1 for _ in range(I)] for _ in range(I)]
        sX, sY = map(int, input().split())
        tX, tY = map(int, input().split())

        matrix[sY][sX] = 0
        queue = deque()
        queue.append((sX, sY))

        while queue:
            x ,y = queue.popleft()

            if x == tX and tY == y:
                break

            for i in range(len(dx)):
                newX, newY = x + dx[i], y + dy[i]

                if newX >= 0 and newX < I and newY >= 0 and newY < I:
                    if matrix[newY][newX] == -1:
                        matrix[newY][newX] = matrix[y][x] + 1
                        queue.append((newX, newY))

        print(matrix[tY][tX])

#https://www.acmicpc.net/problem/2573
from collections import deque
def solve2573():
    Y, X = map(int, input().split())
    matrix = []

    for i in range(Y):
        matrix.append(list(map(int, input().split())))

    def count_island():
        m = [[matrix[i][j] for j in range(X)] for i in range(Y)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def dfs(x, y):
            queue = deque()
            queue.append((x, y))

            while queue:
                _x, _y = queue.pop()
                m[_y][_x] = 0

                for i in range(4):
                    nX, nY = _x + dx[i], _y + dy[i]

                    if nX >= 0 and nX < X and nY >= 0 and nY < Y:
                        if m[nY][nX] != 0:
                            queue.append((nX, nY))

        num_island = 0
        for i in range(Y):
            for j in range(X):
                if m[i][j] != 0:
                    num_island += 1
                    dfs(j, i)

        return num_island

    def update_surface():
        xx = [1, -1 ,0, 0]
        yy = [0, 0, 1, -1]
        surface = [[0 for _ in range(X)] for _ in range(Y)]

        for y in range(Y):
            for x in range(X):
                for i in range(len(xx)):
                    _xx, _yy = x + xx[i], y + yy[i]

                    if _xx >= 0 and _xx < X and _yy >= 0 and _yy < Y:
                        if matrix[_yy][_xx] == 0:
                            surface[y][x] += 1
        return surface

    num_days = 0

    while count_island() == 1:
        num_days += 1
        melting = update_surface()

        for y in range(Y):
            for x in range(X):
                matrix[y][x] = max(0, matrix[y][x] - melting[y][x])

    print(num_days)

solve2573()






