
n, m = map(int,input().split())
a = list(map(int, input().split()))

a.sort() #오름차순
#m이 몇번째인지
lt = 0
rt = n-1

while lt<=rt :
  mid = (lt+rt)//2
  if a[mid] == m :
    print(mid+1) #mid는 인덱스니까
    break
  elif a[mid] > m :
    rt = mid-1
  else:
    lt = mid+1

    