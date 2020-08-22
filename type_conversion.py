#birth_year = input('What is your birth year: ')
#age = 2020 - birth_year
#print('You are ' + age + ' years old')
# running the above code will give you a 'TypeError'. Here is how to fix it

# we have some methods that help to convert from one type to the other
# they are int(), str(), float(), bool()
#birth_year = input('What is your birth year: ')
#age = 2020 - int(birth_year)
#print('You are ' + str(age) + ' years old')

# here is another example that converts a Users weight and converts it to pounds
name = input('What is your name? ')
w_pounds = input('What is your weight in pounds? ')
unit_per_kilogram = 0.45359237
w_kilograms = float(w_pounds) * unit_per_kilogram
print(name + ', you weigh ' + str(w_kilograms) + 'kg')
