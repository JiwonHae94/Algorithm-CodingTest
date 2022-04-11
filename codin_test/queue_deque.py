# https://www.acmicpc.net/problem/2164
from collections import deque
def solve2165():
    N = int(input())
    d = deque([i+1 for i in range(N)])
    cnt = 0

    while len(d) > 1:
        c = d.popleft()

        if cnt % 2 != 0:
            d.append(c)
        cnt += 1

    print(d.pop())

# https://www.acmicpc.net/problem/18258
import sys
from collections import deque
def solve18258():
    N = int(input())
    d = deque()

    for _ in range(N):
        inst = sys.stdin.readline().split()

        if len(inst) > 1:
            n = int(inst[1])
        inst = inst[0]

        if inst == "push":
            d.append(n)
        elif inst == "pop":
            print(d.popleft()) if len(d) > 0 else print(-1)
        elif inst == "size":
            print(len(d))
        elif inst == "empty":
            isEmpty = 1 if len(d) == 0 else 0
            print(isEmpty)
        elif inst == "front":
            if len(d) > 0:
                print(d[0])
            else :
                print(-1)
        elif inst == "back":
            if len(d) > 0:
                print(d[-1])
            else :
                print(-1)

# https://www.acmicpc.net/problem/11650
from collections import deque
import sys
def solve11650():
    T = int(input())
    Q = deque()

    for _ in range(T):
        x, y = map(int, sys.stdin.readline().split())
        Q.append((x, y))

    for x,y in sorted(Q, key = lambda x : (x[0], x[1])):
        print(x, y)

# https://www.acmicpc.net/problem/11651
from collections import deque
import sys
def solve11651():
    T = int(input())
    Q = deque()

    for _ in range(T):
        x, y = map(int, sys.stdin.readline().split())
        Q.append((x, y))

    for x,y in sorted(Q, key = lambda x : (x[1], x[0])):
        print(x, y)

# https://www.acmicpc.net/problem/1181
from collections import deque
import sys
def solve11651():
    T = int(input())
    Q = deque()

    for _ in range(T):
        x = sys.stdin.readline().strip()

        if x not in Q:
            Q.append(x)

    for x in sorted(Q, key = lambda x : (len(x), x)):
        print(x)

# https://www.acmicpc.net/problem/10814
from collections import deque
import sys
def solve10814():
    T = int(input())
    Q = deque()

    for _ in range(T):
        age, name = sys.stdin.readline().strip().split()
        Q.append((int(age), name))

    for x, y in sorted(Q, key = lambda x : x[0]):
        print(x, y)

# https://www.acmicpc.net/problem/18870
from collections import deque
import sys
def solve18870():
    _ = input()
    Q = list(map(int, sys.stdin.readline().strip().split()))
    ans = Q.copy()
    keyMap = {val:idx for idx, val in enumerate(sorted(set(Q)))}
    ans = [str(keyMap[val]) for val in ans]
    print(" ".join(ans))

# https://www.acmicpc.net/problem/10989
from collections import deque
import sys
def solve10989():
    T = int(input())
    Q = [0 for _ in range(10001)]

    for _ in range(T):
        num = int(sys.stdin.readline().strip())
        Q[num] += 1

    for i in range(1, len(Q)):
        if Q[i] != 0:
            for j in range(Q[i]):
                print(i)


solve10989()