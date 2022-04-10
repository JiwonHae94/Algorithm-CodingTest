# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
def solve2108():
    N = int(sys.stdin.readline().strip())
    li = []

    for _ in range(N):
        li.append(int(sys.stdin.readline().strip()))

    li.sort()
    print(round(sum(li) / len(li)))
    print(li[int((len(li) + 1) / 2) - 1])

    c = Counter(li)
    mode = [key for key, value in c.items() if value == c.most_common(1)[0][1]]
    if len(mode) > 1:
        print(mode[1])
    else:
        print(mode[0])

    print(max(li) - min(li))

#https://www.acmicpc.net/problem/1427
import sys
def solve1427():
    N = map(int, sys.stdin.readline().strip())
    print("".join(map(str, sorted(N, reverse = True))))

solve1427()