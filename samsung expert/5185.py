#testcase
t = int(input())
for i in range(t) :
  n, num = input().split()
  n = int(n)
  num = int(num, 16)
  num = format(num, 'b')
  if len(num) == 4*n:
    print("#%d %s"%(i+1, num))
  else :
    for j in range(4*n-len(num)):
      num = '0'+num
    print("#%d %s" % (i+1, num))

