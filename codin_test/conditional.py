# https://www.acmicpc.net/problem/2525
def solve2525():
    H, M = map(int, input().split())
    m = int(input())

    t = H * 60 + M + m

    conversion = lambda x : x - 24 if(x >= 24) else x
    print(conversion(t // 60), t % 60)

# https://www.acmicpc.net/problem/2480
def solve2480():
    X, Y, Z = sorted(map(int, input().split()))

    if X == Y == Z:
        return print(10000 + X * 1000)
    elif X == Y:
        return print(1000 + X * 100)
    elif Y == Z:
        return print(1000 + Y * 100)
    else:
        return print(Z * 100)

solve2480()
