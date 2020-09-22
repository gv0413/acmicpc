def DFS(x) :
  if x == 1:
    print(x)
    return
  else:
    if x%2 == 0:
      print(x)
      DFS(x//2)
    else :
      print(x)
      DFS(3*x+1)

n = int(input())
DFS(n)