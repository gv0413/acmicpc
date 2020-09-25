n , m = map(int, input().split())
global ch, res, cnt
ch = [0]*n
res = [-1] * m
cnt = 0

def DFS(L,s):
  global ch, res, cnt
  if L >= m:
    cnt+=1
    for x in res:
      print(x, end=' ')
    print()
  else:
    for i in range(s,n+1):
      if ch[i-1] == 0 :
        ch[i-1] = 1
        res[L] = i
        DFS(L+1, i+1)
        ch[i-1] = 0

DFS(0,1)

print(cnt)