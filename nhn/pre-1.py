n = int(input())

global chk, g

g = [0 for _ in range(n)]
for i in range(0,n) :
  g[i] = list(map(int, input().split()))  

print(g)
chk = [[0]*n for _ in range(n)]
cnt = list()

#현재 정점에서 오른쪽이나 아래로 이동할 수 있으면 이동하는 재귀뽕뽕
def DFS(u, v, cntIdx) :
  if chk[u][v]:
    return
  
  chk[u][v] = 1
  cnt[cntIdx] +=1
  
  if u+1 < n and g[u+1][v] == 1 and not chk[u+1][v]:
    DFS(u+1, v, cntIdx)
  
  if v+1 < n and g[u][v+1] == 1 and not chk[u][v+1]:
    DFS(u, v+1, cntIdx)

# 금지 : 일단은

for u in range(n):
  for v in range(n):
    if g[u][v] == 1 and not chk[u][v]:
      cnt.append(0)
      DFS(u, v, len(cnt)-1)

if len(cnt) == 0 :
  print(0)
else:
  print(len(cnt))
  cnt.sort()
  print(' '.join(map(str, cnt)))


6
011000
011011
000011
000011
110010
111000
