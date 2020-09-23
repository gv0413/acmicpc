n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse = True)
m = int(input())
global min
min = 10001

def DFS(L, sum):
  global min
  if L > min :
    return
  if m <= sum:
    if sum == m:
      if min > L:
        min = L
  else:
    for i in coin:
      DFS(L+1, sum+i)

DFS(0,0)
print(min)