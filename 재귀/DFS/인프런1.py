def DFS(v) :
  if arr.index(v) == n-1:
    for i in range(0, n) :
      if ch[i] == 1:
        print(i, end='')
    return
  else:
    ch[arr.index(v)] = 1
    if arr.index(v) != n-1:
      DFS(arr[arr.index(v)+1])
    ch[arr.index(v)] = 0
    if arr.index(v) != n-1:
      DFS(arr[arr.index(v)+1])
    
n = int(input())
arr = list(map(int, input().split()))

ch = [0]*n
DFS(arr[0])
