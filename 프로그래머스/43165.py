global numbers, target, n, cnt
target = int(input())
numbers = list(map(int, input().split()))
cnt = 0
n = len(numbers)

def DFS(L, sum) :
  global numbers, target, n, cnt
  if n == L :
    if target == sum :
      print(sum)
      cnt+=1
  else :
    # sum += numbers[L]
    print(L, n, sum, '+',numbers[L])
    DFS(L+1, sum+numbers[L])
    # sum -= numbers[L]*2
    print(L, n, sum, '-', numbers[L])
    DFS(L+1, sum-numbers[L])


DFS(0,0)
print(cnt)