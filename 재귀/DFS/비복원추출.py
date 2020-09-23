n,m = map(int, input().split())

global res , pocket
res = [0]*m
pocket = [1]*n

def DFS(L) :
  global res
  if L>=m :
    for k in res:
      print(k, end=' ')
    print()
    return
  else:
    for i in range(1,n+1) :
      # 주머니에 공이 있나 없나 확인
      if pocket[i-1] == 1 :
        # 공을 빼고 
        pocket[i-1] = 0
        res[L] = i
        DFS(L+1)
        #공을 넣고 사용해
        pocket[i-1] = 1

DFS(0)
