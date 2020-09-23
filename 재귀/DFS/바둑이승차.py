global res
res = 0
c, n = map(int, input().split())
arr = []
sum = 0
for i in range(n):
  tmp = int(input())
  arr.append(tmp)

def DFS(L, sum) :
  global res
  if L==n :
    if c >= sum:
      if res<sum :
        res = sum
    else:
      return;
  else:
    DFS(L+1, sum+arr[L])
    DFS(L+1, sum)

DFS(0,0)
print(res)
