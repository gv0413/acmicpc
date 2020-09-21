def solution(arr):
    _arr = []
    prev = [-1]
    for i in arr :
      if prev[-1] != i :
        _arr.append(i)
      prev.append(i)

    return _arr

arr =[1,1]	
print(solution(arr))