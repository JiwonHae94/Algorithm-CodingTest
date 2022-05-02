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

# https://www.acmicpc.net/problem/1085
def solve1085():
    x, y, w, h = map(int, input().split())

    sX, sY = 0, 0
    dist = min(abs(x - sX), abs(x- w), abs(y - sY), abs(y - h))
    print(dist)

# https://www.acmicpc.net/problem/3009
def solve3009():
    xs = []
    ys = []

    for i in range(3):
        x, y = map(int, input().split())
        if x in xs:
            xs.remove(x)
        else:
            xs.append(x)

        if y in ys:
            ys.remove(y)
        else:
            ys.append(y)

    print(xs[0], ys[0])

# https://www.acmicpc.net/problem/4153
def solve4153():
    while True:
        edges = sorted(list(map(int, input().split())))

        if edges[0] == edges[1] == edges[2] == 0:
            break

        edges = [i*i for i in edges]
        ans = "right" if edges[0] + edges[1] == edges[2] else "wrong"
        print(ans)
# https://www.acmicpc.net/problem/4948
def solve4948():
    N = 123456 * 2
    m = int(N)
    s = [True] * (N + 1)
    s[1] = False

    for i in range(2, m + 1):
        if s[i]:
            for j in range(i + i, N + 1, i):
                s[j] = False

    while True:
        I = int(input())
        if I == 0:
            break

        temp = s[I+1: I * 2+1]
        print(temp.count(True))

# https://www.acmicpc.net/problem/9020
def solve9020():
    N = 10000
    s = [True] * (N + 1)
    s[1] = False
    primes = []

    for i in range(2, N + 1):
        if s[i]:
            primes.append(i)
            for j in range(i + i, N + 1, i):
                s[j] = False

    sums = {}

    for i in primes:
        for j in primes:
            num = i+j

            if num not in sums:
                sums[num] = (i, j)
            else:
                if abs(sums[num][1] - sums[num][0]) > abs(j - i):
                    sums[num] = (i, j)

    T = int(input())
    for _ in range(T):
        number = int(input())
        print(sums[number][0], sums[number][1])

# https://www.acmicpc.net/problem/3053
import math

def solve3053():
    R = int(input())
    print("{0:.6f}".format(math.pi * R ** 2))
    print("{0:.6f}".format(2 * R ** 2))

# https://www.acmicpc.net/problem/5086
def solve5086():

    while True:
        A, B = map(int, input().split())

        if(A == B == 0):
            break

        if (A % B == 0):
            print("multiple")
        elif (B % A == 0):
            print("factor")
        else:
            print("neither")

# https://www.acmicpc.net/problem/1037
def solve1037():
    N = input()
    factors = list(map(int, input().split()))
    print(min(factors) * max(factors))

# https://www.acmicpc.net/problem/1934
def solve1934():
    N = int(input())

    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    for _ in range(N):
        A, B = map(int, input().split())
        print(lcm(A, B))

# https://www.acmicpc.net/problem/2609
def solve2609():
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    A, B = map(int, input().split())
    print(gcd(A, B))
    print(lcm(A, B))

# https://www.acmicpc.net/problem/3036
def solve3036():
    N = int(input())
    rings = list(map(int, input().split()))

    def gcd(x, y):
        if y == 0:
            return x
        else :
            return gcd(y, x % y)

    for i in range(1, N):
        _gcd = gcd(rings[0], rings[i])
        print(f"{rings[0] // _gcd}/{rings[i] // _gcd}")

# https://www.acmicpc.net/problem/11050
def solve11050():
    def factorial(x):
        rslt = 1
        for i in range(2, x+1):
            rslt *= i

        return rslt

    A, B = map(int, input().split())
    print(factorial(A) // factorial(B) // factorial(A-B))


# https://www.acmicpc.net/problem/11051
def solve11051():
    def factorial(x):
        rslt = 1
        for i in range(2, x+1):
            rslt *= i
        return rslt

    A, B = map(int, input().split())
    print((factorial(A) // factorial(B) // factorial(A-B)) % 10007)

# https://www.acmicpc.net/problem/1010
def solve1010():
    N = int(input())

    def factorial(x):
        rslt = 1
        for i in range(2, x+1):
            rslt *= i
        return rslt

    def coefficient(A, B):
        return factorial(A) // factorial(B) // factorial(A-B)

    for _ in range(N):
        A, B = map(int, input().split())
        print(coefficient(max(A, B), min(A, B)))

# https://www.acmicpc.net/problem/1676
def solve1676():
    N = int(input())
    print(N // 5 + N // 25 + N // 125)

# https://www.acmicpc.net/problem/2004
def solve2004():
    def get_five_power_n(n):
        cnt = 0

        while n >= 5:
            cnt += n // 5
            n //= 5

        return cnt

    def get_two_power_n(n):
        cnt = 0
        while n >= 2:
            cnt += n // 2
            n //= 2

        return cnt

    A, B = map(int, input().split())
    cnt5 = get_five_power_n(A) - get_five_power_n(A- B) - get_five_power_n(B)
    cnt2 = get_two_power_n(A) - get_two_power_n(A- B) - get_two_power_n(B)

    print(min(cnt2, cnt5))

solve2004()