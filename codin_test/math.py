# https://www.acmicpc.net/problem/18108
def solve1808():
    diff = 1998 - 2541
    n = int(input())
    print(n + diff)

# https://www.acmicpc.net/problem/10926
def solve10926():
    name = input()
    print(name + "??!")

# https://www.acmicpc.net/problem/1193
import sys
def solve1193():
    N = int(sys.stdin.readline().strip())
    num = 0
    variable_add = 1
    n = 0

    while num < N:
        num += variable_add
        n += 1
        variable_add += 1

    first_index = num - (variable_add - 1) + 1
    N_th = N - first_index

    if n % 2 == 0:
        a = 1 + N_th
        b = n - N_th
    else:
        a = n - N_th
        b = 1 + N_th

    print(f"{a}/{b}")

# https://www.acmicpc.net/submit/10757
def solve10757():
    a, b = map(int, input().split())
    print(a +b )

# https://www.acmicpc.net/problem/2775
def solve2775():
    N = int(input())

    for _ in range(N):
        k = int(input())
        n = int(input())

        floors = [[i+1 for i in range(n + 1)]]

        for i in range(1, k+1):
            prev = floors[i-1]
            current = [sum(prev[0:i+1]) for i in range(n)]
            floors.append(current)

        print(floors[-1][-1])

# https://www.acmicpc.net/problem/10250
def solve10250():
    T = int(input())

    for _ in range(T):
        H, W, N = map(int, input().split())

        def getFloor():
            cnt = 0

            for i in range(1, W+1):
                for j in range(1, H+1):
                    cnt += 1

                    if cnt == N:
                        return (j,i)
        F, R = getFloor()
        print(f"{F}{R:02}")

# https://www.acmicpc.net/problem/2581
def solve2581():
    M = int(input())
    N = int(input())

    def isPrime(n):
        if n == 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    primes = []

    for i in range(M, N+1):
        if isPrime(i):
            primes.append(i)

    if not primes:
        print(-1)
        return

    print(sum(primes))
    print(min(primes))



# https://www.acmicpc.net/problem/1929
# https://velog.io/@htchoi1006/파이썬-에라토스테네스의-체
# 시간 제약 때문에 해당 알고리즘을 사용해야 한다
def solve2581():
    M, N = map(int, input().split())
    m = int(N ** 0.5)
    s = [True] * (N + 1)
    s[1] = False

    for i in range(2, m + 1):
        if s[i]:
            for j in range(i+i, N+1, i):
                s[j] = False

    for i in range(M, N + 1):
        if s[i]:
            print(i)

# https://www.acmicpc.net/problem/11653
def solve11653():
    N = int(input())

    while N != 1:
        div = 1
        for i in range(2, N):
            if N % i == 0:
                div = i
                break

        if div == 1:
            break
        N = int(N/ div)
        print(div)

    if N != 1 :
        print(N)

# https://www.acmicpc.net/problem/1002
def solve1002():
    T = int(input())

    for i in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        d = pow(((x2 - x1) ** 2 + (y2 - y1) ** 2), 0.5)

        if x1 == x2 and y1 == y2:
            if r1 == r2:
                print(-1)
            else:
                print(0)
        else :
            if r1 > d + r2 or r2 > d + r1 or d > r1 + r2:
                print(0)
            elif abs(r1 - r2) == d or r1 + r2 == d:
                print(1)
            else:
                print(2)

solve1002()