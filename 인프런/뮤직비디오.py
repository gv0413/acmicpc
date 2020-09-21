n, m = map(int, input().split())
a = list(map(int, input().split()))
maxx = max(a)

def Count(capacity) :
  cnt = 1
  sum = 0
  for x in a :
    if sum + x > capacity : #용량 초과
      cnt+=1
      sum = x
    else :
      sum +=x
  return cnt   

a.sort()
lt = 1
rt = sum(a)
res = 0

while lt<=rt :
  mid = (lt+rt)//2
  if mid >= maxx and Count(mid) <= m : 
    rt = mid-1
    res = mid
  else:
    lt = mid+1

print(res)
