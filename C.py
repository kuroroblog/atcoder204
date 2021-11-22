import sys

# 再帰の上限数を設定する。
# 参考 : https://note.nkmk.me/python-sys-recursionlimit/
sys.setrecursionlimit(10000)

# 標準入力を受け付ける。
N, M = map(int, input().split())

def dfs(temp, i):
    # 一度ゴールとして認めたものを再度更新しない。
    if temp[i]:
        return
    temp[i] = True

    # ゴールとして認めることのできる都市を探す。
    for to in edges[i]:
        dfs(temp, to)

# 都市間の移動情報を格納する。
# edges[0]は利用しない。
edges = []
for _ in range(N + 1):
    edges.append([])

for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)

# スタート地点とゴール地点の都市の組数の合計値を格納する。
cnt = 0
# スタート地点になる都市として、1~Nが考えられるのでrange(1, N + 1)とする。
for i in range(1, N + 1):
    # ゴール地点として認めたものか判断する変数。
    # temp[0]は利用しない。
    temp = [False] * (N + 1)
    dfs(temp, i)

    # ゴール地点と認めた数だけ足し合わせる。
    cnt += sum(temp)

print(cnt)
