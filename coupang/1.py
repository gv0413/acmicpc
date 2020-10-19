n = int(input())

def f(n, k):
  res = ''
  mul = 1
  if n >= 1:
    # print(n % k, end='')
    res = f(n//k, k) + str(n % k)
  return res


for i in range(2, 10) :
  mul = 1
  cur = f(n, i)
  for j in cur :
    if j != '0':
      mul *= int(j)
  print(mul)