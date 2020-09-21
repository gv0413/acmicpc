def solution(orders, course):
    answer = []
    order_sort = ''
    order_arr = []
    for i in orders : 
        order_sort+=i
        order_arr = list(map(str,order_sort))
    order_arr.sort()

    count_arr = []
    print(order_sort)
    print(order_arr)


    return answer


orders= ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))