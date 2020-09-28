
global res, ch, ct, cp, n
n = int(input())
ct = [0] * n
cp = [0] * n
for i in range(n) :
  ct[i], cp[i] = map(int, input().split())

curDay = 1
ch = [0] * n
print(ct)
print(cp)
res = 0

def DFS(L, time, price) :
  global res, ch, ct, cp, n
  if time+ct[L] > n:
    return
  if L==n :
    if res <= price :
      print(ch, res)
      res = price
  else :
    if ch[L] == 0 :
      if time+ct[L] <= n:
        for i in range(L,L+ct[L]) :
          ch[i] = 1
        DFS(L+1, time+ct[L], price+cp[L])
      for i in range(L, L+ct[L]):
        ch[i] = 0
      DFS(L+1, time, price)
    else:
      DFS(L+1, time, price)

DFS(0,0,0)
print(res)
