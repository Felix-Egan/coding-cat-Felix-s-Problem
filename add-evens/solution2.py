def add_evens(numbers):
    list1 = []
    for x in range(len(numbers)):
        if numbers[x] % 2 == 0:
            list1 = list1 + [numbers[x]]
    return numbers + [sum(list1)]
