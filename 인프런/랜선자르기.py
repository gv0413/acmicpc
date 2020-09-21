# 결정알고리즘관련 문제는 이분검색 쓴다
# 특정 범위 안에 있다는 것을 알 때 사용해본다
# 답을 정해놓고 그 값이 유효하냐 안하냐를 확인
# 답이 되면 범위를 좁혀서 절반을 날리면서 좁혀나간다
# logN 

# 랜선중 가장 큰 랜선 사이에 한개의 랜선 길이가 있겠죠
def Count(len):
  cnt = 0
  for x in Line:
    cnt += (x//len) #작은 토막의 개수. ex.802//187
  return cnt

k, n = map(int, input().split())
Line = []
res = 0
#가장 긴 랜선
largest = 0

for i in range(k):
  tmp = int(input())
  Line.append(tmp)
  largest = max(largest, tmp)

lt = 1
rt = largest

while lt<=rt :
  mid = (lt+rt)//2
  # mid가 한개의 길이 값이라고 생각
  if Count(mid) >= n : #갯수 리턴
    res = mid
    lt = mid+1
  else : 
    rt = mid-1

print(res)