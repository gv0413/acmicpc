a=[0]*3
print(a)

a = [[0]*3 for _ in range(3)]
print(a)
# 000 000 000

a[0][1] = 1 #010 000 000
a[1][1] = 2 #010 020 000

print(a)

for x in a :
  for y in x:
    print(y, end=' ')
  print()
