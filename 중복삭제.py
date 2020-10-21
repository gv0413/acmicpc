def deleteDuplication(inputArr) :
  new_list = list()
  for i in inputArr :
    if i not in new_list :
      new_list.append(i)
  print(new_list)

deleteDuplication([3,4,1,5,3,4,1,5])