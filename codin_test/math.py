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

solve1193()