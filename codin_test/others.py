
#https://www.acmicpc.net/problem/2839
def solve2839():
    target = int(input())
    cnt = 0

    while target >= 0:
        if target % 5 == 0:
            cnt += target // 5
            print(cnt)
            return
        target -= 3
        cnt += 1
    print(-1)

#https://www.acmicpc.net/problem/5622
def solve5622():
    word = input()
    word_map = {
        "A" : 2, "B" : 2, "C" : 2,
        "D" : 3, "E" : 3, "F" : 3,
        "G" : 4, "H" : 4, "I" : 4,
        "J" : 5, "K" : 5, "L" : 5,
        "M" : 6, "N" : 6, "O" : 6,
        "P" : 7, "Q" : 7, "R" : 7, "S" : 7,
        "T" : 8, "U" : 8, "V" : 8,
        "W" : 9, "X" : 9, "Y" : 9, "Z" : 9
    }

    num_sec = 0
    for i in word:
        if i not in word_map:
            num_sec += 11
        else:
            num_sec += word_map[i] + 1
    print(num_sec)

#https://www.acmicpc.net/problem/2750
import heapq
def solve2750():
    n = int(input())
    a = []

    for i in range(n):
        heapq.heappush(a, int(input()))

    while a:
        print(heapq.heappop(a))

#https://www.acmicpc.net/problem/10817
def solve10817():
    s = list(map(int, input().split()))
    heapq.heapify(s)

    heapq.heappop(s)
    print(heapq.heappop(s))

#https://www.acmicpc.net/problem/10872
def solve10872():
    n = int(input())
    memo = [1] + [i+1 for i in range(n)]

    for i in range(1, n+1):
        memo[i] = memo[i-1] * i

    print(memo[n])

#https://www.acmicpc.net/problem/1978
def solve1978():
    n = int(input())

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    nums = list(map(int, input().split()))
    nums = [is_prime(i) for i in nums]
    print(nums.count(True))

#https://www.acmicpc.net/problem/2440
def solve2440():
    n = int(input())

    for i in range(n, 0, -1):
        print("*" * i)

#https://www.acmicpc.net/problem/2441
def solve2441():
    n = int(input())

    for i in range(n, 0, -1):
        s = (" " * (n-i)) + ("*" * i)
        print(s)

# https://www.acmicpc.net/problem/2292
def solve2292():
    n = int(input())
    start = 1
    last = 0

    while True:
        if n > start:
            last += 1
            start = start + last * 6
        else:
            print(last + 1)
            break

#https://www.acmicpc.net/problem/1712
def solve1712():
    A, B, C = map(int, input().split())

    if B >= C:
        print(-1)
        return

    print(A // (C - B) + 1)

#https://www.acmicpc.net/problem/9012
def solve9012():
    n = int(input())

    def checkVPS(s):
        while "()" in s:
            s = s.replace("()", "")
        return not s

    for i in range(n):
        s = input()
        rslt = checkVPS(s)
        print("YES" if rslt else "NO")

#https://www.acmicpc.net/problem/1316
def solve1316():
    n = int(input())

    def isGroupWord(s):
        visited = []

        for i in s :
            if not visited:
                visited.append(i)
            else:
                if i not in visited:
                    visited.append(i)
                else:
                    if visited[-1] != i:
                        return False
        return True

    rslt = 0

    for i in range(n):
        s = input()
        if isGroupWord(s):
            rslt += 1
    print(rslt)

#https://www.acmicpc.net/problem/2751
import heapq
import sys

def solve2751():
    n = int(input())
    nums = []

    for i in range(n):
        num = sys.stdin.readline()
        nums.append(int(num))

    heapq.heapify(nums)

    for i in range(n):
        print(heapq.heappop(nums))

solve2751()