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
