def odd_range(end):
    return [x for x in range(end+1) if x % 2 != 0]


print(odd_range(11))
