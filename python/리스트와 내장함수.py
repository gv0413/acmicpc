import random as r
a=[]
print(a)
b=list()

a=[1, 2, 3, 4, 5]
a.append(6) #123456
print(a)

a.insert(3, 7) #3번 인덱스에 7 들어가서 1237456
print(a)

a.pop() #맨 뒤꺼 하나 빼준다
a.pop(3) #3번 index 값 빼준다.
print(a)

a.remove(4) #4라는 값을 제거해라
print(a)

print(a.index(5)) #5라는 값의 인덱스를 찾아서 리턴 :3

a=list(range(1,11))
print(a)

print(sum(a))
print(max(a)) #a중 가장 큰 값 찾아 리턴. 10
print(min(a))

r.shuffle(a)
print(a)

a.sort() #오름차순
print(a)
a.sort(reverse=True) #내림차순
print(a)

a.clear() #리스트를 비운다
print(a)

a=[23, 12, 36, 53, 19]

for x in enumerate(a): # 튜플. (0,23)처럼 0번 인덱스에 23값이 있다 라는 식으로 넘겨준다
  print(x) 

for x in enumerate(a):
  print(x[0], x[1]) 
print()

for index, value in enumerate(a):
  print(index, value)
print()

if all(60>x for x in a): # a를 돌면서 60>x가 모두 참이면, all은 참을 리천한다.
  print("Yes")
else:
  print("NO")


if any(15>x for x in a): # a를 돌면서 15>x가 한 번이라도 참이 되면 true를 리턴한다.
  print("Yes")
else:
  print("NO")