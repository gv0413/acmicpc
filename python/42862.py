def solution(n, lost, reserve):
  
  for i in lost:
    for j in reserve :
      if i == j :
        lost.remove(i)
        reserve.remove(j)

  
  for i in reserve:
    for j in lost:
      if abs(i-j) == 1 :
        lost.remove(j)
        break


  answer = n-len(lost)
  return answer

lost = [2,4]
reserve = [3]
print(solution(5, lost, reserve))
