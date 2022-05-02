# https://www.acmicpc.net/problem/15649
import sys
def solve15649():
    # N = range
    # M = size of the combination
    N, M = map(int, sys.stdin.readline().strip().split())

    def backtrack(x, y):
        if y == M:
            print(" ".join(x))
            return

        for i in range(1, N + 1):
            if str(i) not in x:
                x.append(str(i))
                backtrack(x, y + 1)
                x.pop()

    backtrack([], 0)

# https://www.acmicpc.net/problem/15650
import sys
def solve15650():
    N, M = map(int, sys.stdin.readline().strip().split())
    ans = []
    def backtrack(x, y):
        if y == M:
            sX = sorted(x)
            if sX not in ans:
                ans.append(sX)
            return

        for i in range(1, N + 1):
            if str(i) not in x:
                x.append(str(i))
                backtrack(x, y + 1)
                x.pop()

    backtrack([], 0)
    for i in ans:
        print(" ".join(i))

# https://www.acmicpc.net/problem/15651
import sys
def solve15651():
    N, M = map(int, sys.stdin.readline().strip().split())
    ans = []
    def backtrack(x, y):
        if y == M:
            ans.append(" ".join(x))
            return

        for i in range(1, N + 1):
            x.append(str(i))
            backtrack(x, y + 1)
            x.pop()

    backtrack([], 0)
    for i in ans:
        print(i)

# https://www.acmicpc.net/problem/15652
import sys
from collections import Counter
def solve15652():
    N, M = map(int, sys.stdin.readline().strip().split())
    nums = []

    def dfs(idx):
        if len(nums) == M:
            print(*nums)
            return

        for i in range(idx, N + 1):
            nums.append(i)
            dfs(i)
            nums.pop()

    dfs(1)

# https://www.acmicpc.net/problem/9663
def solve9663():
    N = int(input())
    answer = 0
    visited = [False] * N
    row = [0] * N

    def is_promising(x):
        for i in range(x):
            # row[x] == row[i] : column이 같은 경우 확인
            # abs(row[x] - row[i]) == abs(x - i) -> check diagonal
            if row[x] == row[i] or abs(row[x] - row[i]) == abs(x- i):
                return False
        return True

    def n_queens(x):
        if x == N:
            nonlocal answer
            answer += 1
            return

        for i in range(N):
            if visited[i]:
                continue
            row[x] = i
            if is_promising(x):
                visited[i] = True
                n_queens(x + 1)
                visited[i] = False

    n_queens(0)
    print(answer)

# https://www.acmicpc.net/problem/2580
import sys
def solve2580():
    matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
    blacks = []

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                blacks.append((i, j))

    def check_row(x, a):
        for i in range(9):
            if a == matrix[x][i]:
                return False
        return True

    def check_col(y, a):
        for i in range(9):
            if a == matrix[i][y]:
                return False
        return True

    def check_rect(x, y, a):
        nx = x // 3 * 3
        ny = y // 3 * 3

        for i in range(3):
            for j in range(3):
                if a == matrix[nx + i][ny + j]:
                    return False
        return True

    def dfs(idx):
        if idx == len(blacks):
            # all blanks are filled
            for i in range(9):
                print(*matrix[i])
            exit(0)

        for i in range(1, 10):
            x = blacks[idx][0]
            y = blacks[idx][1]

            if check_col(y, i) and check_row(x, i) and check_rect(x, y, i):
                matrix[x][y] = i
                dfs(idx + 1)
                matrix[x][y] = 0
    dfs(0)

