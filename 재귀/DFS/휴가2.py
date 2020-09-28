n = int(input())
ct = [0] * n
cp = [0] * n
for i in range(n):
  ct[i], cp[i] = map(int, input().split())
global res, endDay
endDay = 0
print(ct)
print(cp)
res = 0


def DFS(L, time, price):
  global res, endDay
  if endDay > n:
    return
  if L == n:
    print(L, endDay, price)
    if res <= price:
      print(L, endDay, price)
      res = price
  else:
    if endDay <= L:
      endDay = L + ct[L]
      DFS(L+1, endDay, price+cp[L])
      endDay = L - ct[L]
      DFS(L+1, endDay, price)
    else:
      DFS(L+1, endDay, price)
    
DFS(0, 0, 0)
print(res)
