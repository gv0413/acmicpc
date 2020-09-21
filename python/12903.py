def solution(s):
  answer = ''
  arr = list(s)
  len_arr = len(arr)
  for i in arr :
    if len_arr%2 == 0:
      mid = round(len_arr/2)
      answer = arr[mid-1] + arr[mid]
    else :
      mid = len_arr//2 
      answer = arr[mid]

  return answer

s = "abcde"
print(solution(s))