msg = "It is Time"
print(msg.upper()) #대문자로
print(msg.lower()) #소문자로
tmp = msg.upper()
print(tmp.find('T')) #'T'를 찾아서 인덱스 번호 리턴
print(tmp.count('T')) #'T' count
print(msg[:2]) #문자열의 처음부터 2 앞까지만 뽑아내서 출력한다. 0,1,2번째 인덱스
print(msg[3:5]) #'is' 3번 인덱스부터 4번 인덱스까지
print(len(msg)) #10
print(tmp)

for i in range(len(msg)):
  print(msg[i], end=' ')
print()

for x in msg:
  print(x, end=' ')
print()

for x in msg:
  if x.isupper(): #대문자이면
    print(x, end=' ')
print()

for x in msg:
  if x.islower(): #소문자이면
    print(x, end=' ')
print()

for x in msg:
  if x.isalpha(): #알파벳이면이면
    print(x, end='')
print()

tmp='AZ'
for x in tmp:
  print(ord(x)) #ASCII

#  A:65, Z:90

tmp=65
print(chr(tmp)) #대응되는 문자를 출력