n = int(input())
global g, ch
g = [0 for _ in range(n)]

ch = [[0]*(n) for _ in range(n)]
cnt = list()

for i in range(n) :
  tmp = input()
  g[i] = [int(d) for d in tmp]

def DFS(u,v,cntIdx):
  global ch, g
  if ch[u][v]:
    return
  else:
    ch[u][v] = 1
    cnt[cntIdx] += 1

    if u+1 < n and g[u+1][v] == 1 and not ch[u+1][v]:
      DFS(u+1, v, cntIdx)

    if u-1 >= 0 and g[u-1][v] == 1 and not ch[u-1][v]:
      DFS(u-1, v, cntIdx)

    if v-1 >= 0 and g[u][v-1] == 1 and not ch[u][v-1]:
      DFS(u, v-1, cntIdx)

    if v+1 < n and g[u][v+1] == 1 and not ch[u][v+1]:
      DFS(u, v+1, cntIdx)

for i in range(n):
  for j in range(n):
    if ch[i][j] == 0 and g[i][j] == 1:
      cnt.append(0)
      cntIdx = len(cnt)-1
      DFS(i, j, cntIdx)

if len(cnt) == 0 :
  print(0)
else:
  print(len(cnt))
  cnt.sort()
  for i in range(len(cnt)):
    print(cnt[i])
