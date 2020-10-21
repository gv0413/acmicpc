def isNestedparentheses(s):
  count = 0
  for i in range(0, len(s)) :
    if s[i] == '(' :
      count += 1
    elif s[i] == ')' :
      count -= 1
      if count < 0:
        return False
  
  if count == 0 :
    return True
  else:
    return False

print(isNestedparentheses('()()'))
print(isNestedparentheses('(())'))
print(isNestedparentheses(')('))

