# https://www.acmicpc.net/problem/2231
def solve2231():
    N = int(input())

    get_sum = lambda x :  x + sum(map(int, list(str(x))))

    for i in range(1, N):
        if N == get_sum(i):
            print(i)
            return
    print(0)

# https://www.acmicpc.net/problem/7568
def solve7568():
    T = int(input())
    info = []

    for i in range(T):
        weight, height = map(int, input().split())
        info.append((weight, height))

    def count(width, height):
        return sum(1 for w, h in info if w > width and h > height)

    ranking = [str(count(w, h) + 1) for w, h in info]
    print(" ".join(ranking))

# https://www.acmicpc.net/problem/1018
def solve1018():
    M, N = map(int, input().split())
    grid = []

    for i in range(M):
        grid.append(list(input()))

    correctW = [['B' if (x + y) % 2 ==0 else 'W' for x in range(8)] for y in range(8)]
    correctB = [['W' if (x + y) % 2 ==0 else 'B' for x in range(8)] for y in range(8)]

    ans = float('inf')

    for y in range(M - 7):
        for x in range(N - 7):
            cntA, cntB = 0, 0
            for k in range(8):
                for l in range(8):
                    if grid[y+k][x+l] != correctW[k][l]:
                        cntA += 1

                    if grid[y+k][x+l] != correctB[k][l]:
                        cntB += 1
            ans = min(cntA, cntB, ans)

    print(ans)

# https://www.acmicpc.net/problem/1436
def solve1436():
    N = int(input())
    n = 666
    ans = n

    while N > 0:
        if "666" in str(n):
            N -= 1
            ans = n
        n += 1

    print(ans)
solve1436()