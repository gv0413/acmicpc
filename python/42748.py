def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
      _array = array[commands[i][0]-1:commands[i][1]]
      _array.sort()
      answer.append(_array[commands[i][2]-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))