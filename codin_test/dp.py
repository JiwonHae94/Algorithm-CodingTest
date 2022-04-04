
# https://www.acmicpc.net/problem/1463
def solve1463():
    n = int(input())
    dp = [0 for _ in range(n+1)]

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i // 2] + 1)
        ## not elif for cases that are divisible by both 2 and 3
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[n])

#https://www.acmicpc.net/problem/10870
def solve10870():
    i = int(input())
    memo = [0, 1]

    for i in range(2, i+1):
        memo.append(memo[i-1] + memo[i-2])

    print(memo[i])


#https://www.acmicpc.net/problem/9095
def solve9095():
    n = int(input())

    def count_comb(num):
        if num == 0:
            return 1
        elif num < 1:
            return 0

        out = 0
        candidates = [1, 2, 3]

        for i in candidates:
            out += count_comb(num - i)
        return out

    for i in range(n):
        num = int(input())
        comb_cnt = count_comb(num)
        print(comb_cnt)

#https://www.acmicpc.net/problem/1003
def solve1003():
    n = int(input())
    fib = [[1, 0], [0, 1]]

    for i in range(n):
        temp = fib.copy()
        t = int(input())

        for i in range(2, t+1):
            acc = [temp[i-1][0] + temp[i-2][0], temp[i-1][1] + temp[i-2][1] ]
            temp.append(acc)

        print(temp[t][0], temp[t][1])

# https://www.acmicpc.net/problem/2798
def solve2798():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    def get_max(candidates, partial_sum):
        rslt = 0

        if len(partial_sum) == 3:
            s = sum(partial_sum)
            if s <= M:
                return s
            return 0

        for i in range(len(candidates)):
            cached = candidates[i]
            rslt = max(rslt, get_max(candidates[i+1:], partial_sum + [cached]))

        return rslt

    print(get_max(cards, []))

