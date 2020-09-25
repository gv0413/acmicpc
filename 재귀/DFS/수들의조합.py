n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
res = [0]*k
ch  = [0] * n
cnt=0

def DFS(L,sum,s) :
  global cnt
  if L>=k :
    if sum % m == 0 :
      cnt+=1
      for x in res :
        print(x, end=' ')
      print()
  else:
    for i in range(s, n) :
      if ch[i] == 0:
        ch[i] = 1
        res[L] = arr[i]
        DFS(L+1, (sum+res[L]), s+i)
        ch[i] =0

DFS(0,0,0)
print(cnt)