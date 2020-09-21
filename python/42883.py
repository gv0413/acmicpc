def solution(number, k):
  num_arr = list(map(int, number))
  _arr = list(map(int, number))
  pop_num = 0
  answer = ''
  max_n = max(_arr)
  # for a in _arr :
  #   if a < max_n :
  #     _arr.remove(a)

  #   print(_arr)
  #   if pop_num == k :
  #     break
  #   else :
  #     min_n = min(_arr)
  #     if min == a :
  #       _arr.remove(a)
  #       pop_num += 1

  for i in range(0,k+1) :
    for j in num_arr :
      if pop_num == k:
        break
      elif i == j :
        pop_num +=1
        _arr.remove(j)


  for k in _arr :
    print(k, end='')
  return answer

  

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))