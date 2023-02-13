# count é um iterator sem fim (itertools)
# muito similar ao range, mas o range precisa saber quando vai acabar
from itertools import count

c1 = count(16, 8)
r1 = range(16, 100, 8)

# print(next(c1)) # 1 - 0
# print(next(c1)) # 2 - 1
# print(next(c1)) # 3 - 2
# print(next(c1)) # 4 - 3
# print(next(c1)) # 5 - 4
# print(next(c1)) # 6 - 5

# print('c1', hasattr(c1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))
# print('r1', hasattr(r1, '__iter__'))
# print('r1', hasattr(r1, '__next__'))

print('count:')
for i in c1:
    if i > 100:
        break

    print(i)

print('range:')
for i in r1:
    if i > 100:
        break

    print(i)