n, m = map(int, input().split())
global res, cnt
res = [0]*m
cnt = 0

def DFS(L) :
  global res, cnt
  if L >= m :
    cnt+=1
    for j in res:
      print(j, end=' ')
    print()
    return
  else:
    for i in range(1,n+1) :
      res[L]=i
      DFS(L+1)

DFS(0)
print(cnt)