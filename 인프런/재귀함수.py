# 자기자신을 호출
# 스택을 활용한다.

def DFS(i):
  if i>0:
    DFS(i-1) # 1 2 3
    print(i)
    # DFS(i-1) 3 2 1 


n = int(input())

DFS(n)

