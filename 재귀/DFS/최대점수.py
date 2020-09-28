n, m = map(int, input().split())
global sumScore, time, score, ch
score = [0] * n
time = [0] * n
ch = [0] * n
for i in range(n) :
  score[i], time[i] = map(int, input().split())


maxScore = 0
print(score)
print(time)

# 기뽀니디 ! 


def DFS(L, curScore, curTime):
  global time, score, ch, maxScore
  if L>n:
    return
  elif curTime >= m:
    if maxScore < curScore :
      maxScore = curScore
    return
  else:
    for i in range(0,n) :
      if ch[i] == 0 :
        ch[i] = 1
        if curTime + time[i] <= m:
          DFS(L+1, curScore+score[i], curTime+time[i])
        ch[i] = 0

DFS(0, 0, 0)

print(maxScore)
