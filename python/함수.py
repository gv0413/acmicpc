
def inPrime(x):
  for i in range(2, x):
    if x%i ==0:
      return False
  return True


a=[12, 13, 7, 9, 19]
for y in a:
  if inPrime(y):
    print(y, end=' ')
  

plus_two = lambda x: x+2
print(plus_two(1)) #3
#익명함수..

def plus_one(x):
  return x+1

a=[1,2,3]
print(list(map(plus_one, a))) #a의 값들이 plus_one 함수에 다 들어가는 것이지
print(list(map(lambda x: x+1, a)))

