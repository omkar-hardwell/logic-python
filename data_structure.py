"""List of data structures."""

# 1) List and it's methods
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('List - ', fruits)

print('Count of item(apple) - ', fruits.count('apple'))

print('Count of item(tangerine) - ', fruits.count('tangerine'))

print('List item(banana) index - ', fruits.index('banana'))

# Find next banana starting a position 4
print('Find next banana starting a position 4 - ', fruits.index('banana', 4))

fruits.reverse()
print('Reverse list - ', fruits)

fruits.append('grape')
print('Append data(grape) to list - ', fruits)

fruits.extend(['mango', 'jackfruit'])
print('Extend list[\'mango\', \'jackfruit\'] - ', fruits)

fruits.insert(1, 'dragon fruit')
print('Insert item into list - ', fruits)

fruits.sort()
print('Sort list - ', fruits)

print('List pop - ', fruits.pop())

copy_of_fruits = fruits.copy()
print('Copy of list - ', copy_of_fruits)

fruits.remove('jackfruit')
print('Remove item from list - ', fruits)

print('Clear list - ', fruits.clear())

print('----------------------------------------------------')

# 2) List as queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append('Omkar')
print('Append queue - ', queue)

queue.popleft()
print('Left who first arrives - ', queue)

print('----------------------------------------------------')

# 3) List comprehensions
print('List comprehensions')
print('Table of 2 ', [x * 2 for x in range(1, 10+1)])

matrix = []
print('3 x 3 Matrix ', [[x + 1 for x in range(3)] for i in range(3)])

print('----------------------------------------------------')

# 4) Tuples and Sequences
t = ('male', 'female')
print('Tuple ', t)

v = ([1, 2, 3], [3, 2, 1])
print('Tuple with mutable objects ', v)

print('----------------------------------------------------')

# 5) Sets

