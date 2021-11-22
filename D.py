# <方針>
# 1つのオーブンのみを稼働された場合に、かかる時間を求める。
# 料理の組み合わせを考えて、かかる時間を、動的計画法(dp)を利用してそれぞれ列挙する。
# max(1つのオーブンでかかる時間 - 料理の組み合わせによりかかる時間, 料理の組み合わせによりかかる時間)の、一番小さい時間を求める。
# 参考 : https://qiita.com/u2dayo/items/1ed77ef0ac2cf3de7c15#d%E5%95%8F%E9%A1%8Ccooking

# 標準入力を受け付ける。
N = int(input())

T = list(map(int, input().split()))

# オーブンを1つで稼働させた場合にかかる時間
S = sum(T)

# dp[0][i] : 0個の料理を最短i分で調理することが可能かどうか?
# dp[1][i] : 1個(T0)の料理を最短i分で調理することが可能かどうか?
# dp[2][i] : 2個(T0, T1)の料理を最短i分で調理することが可能かどうか?
# dp[3][i] : 3個(T0, T1, T2)の料理を最短i分で調理することが可能かどうか?
dp = []
for i in range(N + 1):
    dp.append([False] * (S + 1))
# 0個の料理に関しては0分で調理できるためdp[0][0]はTrueになる。
dp[0][0] = True

for i in range(N):
    t = T[i]
    for j in range(S + 1):
        # 一つ前の動的計画法(dp)でok出したものは、okとする。
        if dp[i][j]:
            dp[i + 1][j] = True

        # 一つ前の動的計画法(dp)でokを出した時間 + 今回検証するT[i]の時間に関してokを出す。
        if j - t >= 0 and dp[i][j - t]:
            dp[i + 1][j] = True

ans = 100000000000000
for s in range(S + 1):
    if dp[N][s]:
        # max(1つのオーブンでかかる時間 - 料理の組み合わせによりかかる時間, 料理の組み合わせによりかかる時間)の、一番小さい時間を求める。
        score = max(s, S - s)
        ans = min(ans, score)

print(ans)
