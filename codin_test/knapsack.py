#https://www.acmicpc.net/problem/12865
def solve12865():
    N, K = map(int, input().split())
    wt = []
    vs = []

    for i in range(N):
        w, v = map(int, input().split(" "))
        wt += [w]
        vs += [v]

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(N+1):
        for w in range(K+1):
            if i == 0 or w == 0:
                dp[i][w] = 0 ## 첫번째 행/열은 0으로
            elif wt[i-1] <= w:
                dp[i][w] = max(vs[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w]) # 점화식
            else:
                dp[i][w] = dp[i-1][w]

    print(dp[N][K])

# https://www.acmicpc.net/problem/1535
def solve1535():
    N = int(input())
    K = 100 -1
    tire = list(map(int, input().split()))
    happiness = list(map(int, input().split()))

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(N+1):
        for w in range(K+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif tire[i-1] <= w:
                dp[i][w] = max(happiness[i-1] + dp[i-1][w - tire[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print(dp[N][K])

#https://www.acmicpc.net/problem/9084
def solve9084():
    N = int(input())
    coins = list(map(int, input().split()))
    K = int(input())

    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(len(dp)):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, K + 1):
            if coins[i-1] <= j:
                dp[i][j] = max(dp[i-1][j] + dp[i][j - coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[N][K])
