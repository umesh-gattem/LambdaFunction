list_of_numbers = [1, 2, 33, 6, 98, 56, 89]
numbers = [4, 56, 98, 36, 78, 58, 47]
sum = list(map(lambda x, y: x+y, list_of_numbers,numbers))
print(sum)


# greatest_number = reduce(lambda x, y : x if x>y else y, )
# print(next(greatest_number))


print(list(filter(lambda x: x % 2, list_of_numbers)))


f = lambda x: x+4
print(f(4))

