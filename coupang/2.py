from datetime import datetime
import time
customer = ["02/28 23:59:00 03", "03/01 00:00:00 02", "03/01 00:05:00 10"]
length = len(customer)
ch = [0] * n

def customerToTimeStamp(customer) :
  date = customer.split()[0].split('/')[0] + '-' + customer.split()[0].split('/')[1]
  # print(date)
  spendTime = int(customer.split()[2])
  mdhms = '2020-' + date + ' ' + customer.split()[1]
  # print(mdhms)
  timestamp = time.mktime(datetime.strptime(mdhms, '%Y-%m-%d %H:%M:%S').timetuple())
  # print(timestamp)
  endTime = timestamp + spendTime
  return [timestamp, endTime]

startTime = []
endTime = []
kiosk = [0] * n

for i in customer : 
  startTime.append(customerToTimeStamp(i)[0])
  endTime.append(customerToTimeStamp(i)[1])

print(startTime)
# print(endTime)

startTime.sort()
print(startTime)

for i in range(n):
  if ch[i] == 0:
    ch[i] += 1
    kiosk[i] = [startTime[i],endTime[i]]
    
  if ch[]가 다 같으면
    minIdx = index(min(endTime))
    kiosk[index(min(endTime))] = [startTime[min], endTime[min]]

  if kiosk[i][1] < startTime[i]:
    ch[i] += 1
    kiosk[i] = [startTime[i], endTime[i]]

