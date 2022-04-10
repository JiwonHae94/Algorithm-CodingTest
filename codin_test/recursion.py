# https://www.acmicpc.net/problem/2447
def solve2447():
    N = int(input())
    grid = [[" " for _ in range(N)] for _ in range(N)]

    def star(n, x, y):
        s = n // 3

        if n == 1:
            grid[x][y] = "*"
            return
        else:
            star(s, x, y)
            star(s, x, y+s)
            star(s, x, y+s*2)

            star(s, x+s, y)
            star(s, x+s, y+s*2)

            star(s, x+s*2, y)
            star(s, x+s*2, y+s)
            star(s, x+s*2, y+s*2)

    star(N, 0, 0)

    for _ in grid:
        print("".join(_))

# https://www.acmicpc.net/problem/11729
def solve11729():
    def hanoi_tower(n, start, end):
        if n == 1:
            print(start, end)
            return

        hanoi_tower(n - 1, start, 6 - start - end)  # 1단계
        print(start, end)  # 2단계
        hanoi_tower(n - 1, 6 - start - end, end)  # 3단계

    n = int(input())
    print(2 ** n - 1)
    hanoi_tower(n, 1, 3)

solve11729()