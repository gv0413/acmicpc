
a = [[0 for i in range(20)] for row in range(20)]

# for i in range(n) :
#   x, y = input().split()
#   x = int(x)
#   y = int(y)
#   a[x-1][y-1] = 1
  
for i in range(19):
  for j in range(19):
    a[i][j] = input().split()
    print(a[i][j], sep=' ', end=' ')
  print()

n = int(input())

for i in range(n) :
  x, y = input().split()
  x = int(x)
  y = int(y)
  
# for i in a :
#   for j in a :
#     print(a[i][j])
