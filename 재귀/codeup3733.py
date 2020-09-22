def DFS(x):
  if x == 1:
    arr.append(x)
    return arr
  else:
    if x % 2 == 0:
      arr.append(x)
      DFS(x//2)
    else:
      arr.append(x)
      DFS(3*x+1)

a, b = map(int, input().split())
maxlen = 0
maxIdx = -1
for i in range(a, b+1) :
  arr=[]
  DFS(i)
  if maxlen < len(arr):
    maxlen = len(arr)
    maxIdx = i

print("%d %d" % (maxIdx, maxlen))
