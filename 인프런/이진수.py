def DFS(x) :
  if x>=1 :
    DFS(x//2)
    print(x % 2, end='')

n = int(input())
if n==0 :
  print(0)
else:
  DFS(n)
