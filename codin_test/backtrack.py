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
def solve15652():
    N, M = map(int, sys.stdin.readline().strip().split())
    ans = []
    def backtrack(x, length):
        if length == M:
            ans.append(x.copy())
            return

        for i in range(1, N + 1):
            x.append(i)
            backtrack(x, length + 1)
            x.pop()

    backtrack([], 0)
    for i in ans:
        print(*i)

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

solve9663()