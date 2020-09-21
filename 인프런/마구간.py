def cal(maxDistance) :
  cnt = 1
  prev = x[0]
  for j in x :
    if maxDistance <= j-prev:
      cnt+=1
      prev = j
  return cnt


n,c = map(int, input().split())
x = []
for i in range(n) :
  tmp = int(input())
  x.append(tmp)

x.sort()

lt = 1
rt = max(x)
res = 0

while lt<=rt :
  mid = (lt+rt)//2
  if cal(mid) >= c :
    res = mid
    lt = mid+1
  else:
    rt = mid-1

print(res)

