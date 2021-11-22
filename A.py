# 標準入力を受け付ける。
x, y = map(int, input().split())

# 3人が同じ手の場合
if x == y:
    print(x)
# 3人が異なる手の場合
elif (x == 0 and y == 1) or (x == 1 and y == 0):
    print(2)
# 3人が異なる手の場合
elif (x == 0 and y == 2) or (x == 2 and y == 0):
    print(1)
# 3人が異なる手の場合
else:
    print(0)
