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

solve15652()