n, k = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = n-1

res = 0

while lt<=rt :
  if k > max(arr) :
    res = n+1
    break

  mid = (lt+rt)//2
  if arr[mid] >=k:
    res = mid+1
    rt = mid-1
  else:
    lt = mid+1

print(res)