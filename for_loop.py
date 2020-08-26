# forloops allow you to iterate through strings, numbers, list. e.g
for item in "Python":
    print(item)

# we can loop through a list. e.g
for item in ['Chizom', 'Arum', 'BET', 'Apple']:
    print(item)  # this output's the words individually

# we can loop through numbers e.g
for item in [1, 2, 3, 4, 5]:
    print(item)  # this output's 1,2,3,4,5
print('''
    
    ''')
print('''
    
    ''')

# we can loop throug a rang of number using the range function e.g
for item in range(10):
    print(item)  # this output's 0,1,2,3,4,5,6,7,8,9

print('''
    
    ''')
print('''
    
    ''')

# to print from 5 to 9 we can do the following
for item in range(5, 10):
    print(item)  # this output's 5,6,7,8,9
print('''

''')
print('''

''')

# we can do a step (two steps or 3 steps) using range as it's 3rd argument.
# let's do a 2 step count
for item in range(5, 10, 2):
    print(item)  # this output's 5,7,9
print('''
    
    ''')
print('''
    
    ''')


# this calculates the total number of items in a shoping cart
price_list = [20, 10, 20, 10]
total = 0
for item in price_list:
    total += item
print("Total is: " + str(total))
