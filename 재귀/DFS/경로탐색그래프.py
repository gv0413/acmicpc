# 5 9
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 5
# 3 4
# 4 2
# 4 5

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

global ch, cnt

cnt = 0 
ch = [0] * (n+1)
path=[]

for i in range(m):
  a, b = map(int, input().split())
  g[a][b] = 1

def DFS(v) :
  global ch, cnt, res
  if v == n :
    cnt+=1
    for i in path :
      print(i, end=' ')
    print()
    return
  for i in range(1,n+1) :
    if g[v][i]==1 and ch[i]==0:
      ch[i] = 1
      path.append(i)       
      DFS(i)
      path.pop()
      ch[i] =0

ch[1] = 1
path.append(1)
DFS(1)

print(cnt)
