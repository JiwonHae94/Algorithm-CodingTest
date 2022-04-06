# https://www.acmicpc.net/problem/2447
def solve2447():
    N = int(input())

    for i in range(1, N+1):
        for j in range(1, N+1):
            print("*", end = "")
            # if (j + i * j) % 3 ==0:
            #     print(" ", end ="")
            # else:
            #     print("*", end ="")
        print()

solve2447()