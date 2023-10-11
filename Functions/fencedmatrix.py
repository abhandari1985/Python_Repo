# Fenced Matrix
# m=4, n=5
# 1   1   1   1   1
# 1   0   0   0   1
# 1   0   0   0   1
# 1   1   1   1   1

m = int(
    input(
        "value for m",
    )
)
n = int(
    input(
        "value for n",
    )
)
# start writing code here
final = [0] * n
# [0,0,0,0,0]
final = [list(final) for i in range(m)]
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            final[i][j] = 1
for i in final:
    print(i)
