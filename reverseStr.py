def reverseStr(strInput):
  out = ''
  for i in strInput:
    out = i + out
  print(out)

reverseStr('hello')
