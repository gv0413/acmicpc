n, m = map(int, input().split())
global res, time, score, ch
score = [0] * n
time = [0] * n
for i in range(n):
  score[i], time[i] = map(int, input().split())

global res
res = 0
print(score)
print(time)

def DFS(L, sum, curTime) :
  global res
  if curTime > m:
    return
  if L==n :
    if sum > res :
      res = sum
  else :
    DFS(L+1, sum+score[L], curTime+time[L])
    DFS(L+1, sum, curTime)

DFS(0,0,0)
print(res)
