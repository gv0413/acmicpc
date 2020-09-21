def solution(arr, divisor):
  answer = []
  for i in arr :
    if i % divisor == 0 :
      answer.append(i)
  
  if len(answer) == 0 :
    answer.append(-1)
  answer.sort()
  return answer

arr = [2, 36, 1, 3]
divisor = 1
print(solution(arr, divisor))

def solution(new_id):
  answer = ''
  _id = []
  _id = _id.lower()
  
  return answer