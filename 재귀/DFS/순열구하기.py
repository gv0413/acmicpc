def DFS(L) :
  global res, cnt, pocket
  if L == m :
    cnt+=1
    for i in res :
      print(i, end=' ')
    print()
  else:
    for k in range(1, n+1) :
      if pocket[k-1] == 1:
        pocket[k-1] = 0
        res[L] = k
        DFS(L+1)
        pocket[k-1] =1

n, m = map(int, input().split())
global res, cnt, pocket
res = [0] * m
pocket = [1]*n
cnt = 0
DFS(0)
print(cnt)
