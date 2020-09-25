n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range (n+1)]

for i in range(m):
  a, b, v = map(int, input().split())
  g[a][b] = v


for i in range(1, n+1) :
  for j in range(1, n+1) :
    print(g[i][j], end=' ')
  print() 