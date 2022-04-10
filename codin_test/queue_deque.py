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
