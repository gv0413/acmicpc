import re

def solution(new_id):
  answer = ''
  _id = new_id.lower()
  _id = re.sub('([^a-z0-9._-])', '', _id)
  _id = list(map(str,_id))
  
  prev = '!'
  next = []
  for i in _id :
    if not (i == '.' and i == prev) :
      next.append(i)
    prev = i
  
  _id = next

  if len(_id)>0 and _id[0] == '.' :
    _id.pop(0)
  if len(_id)>0 and _id[len(_id)-1] == '.' :
    _id.pop()
  
  if len(_id) == 0 :
    while len(_id) <3 :
      _id.append('a')
  
  while len(_id) >= 16 :
    _id.pop()
  
  if _id[-1] == '.' :
    _id.pop()

  while len(_id) <3 :
    _id.append(_id[-1])

  for j in _id :
    answer+=j;
  return answer

new_id5 = "abcdefghijklmn.p"
print(solution(new_id5))
