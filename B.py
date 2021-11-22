# 標準入力を受け付ける。
N = int(input())

A = list(map(int, input().split()))

# 木の実の合計数
sum_nuts = 0
for i in range(N):
    # x > 10の時x - 10個木の実を収穫する。
    if A[i] > 10:
        sum_nuts += A[i] - 10

print(sum_nuts)
