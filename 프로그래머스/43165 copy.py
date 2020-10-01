global numbers, target, n
target = int(input())
numbers = list(map(int, input().split()))
n = len(numbers)

def DFS(L, sum) :
  global numbers, target, n
  cnt = 0
  if n == L :
    if target == sum :
      print(sum)
      return 1
  else :
    # sum += numbers[L]
    print(L, n, sum, '+',numbers[L])
    cnt = cnt + DFS(L+1, sum+numbers[L])
    # sum -= numbers[L]*2
    print(L, n, sum, '-', numbers[L])
    cnt = cnt + DFS(L+1, sum-numbers[L])
    return cnt


answer = DFS(0,0)
print(answer)