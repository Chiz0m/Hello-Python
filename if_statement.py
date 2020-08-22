# if statments allows you to set conditions for your application e.g
price_of_house = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price_of_house * 10/100
else:
    down_payment = price_of_house * 20/100

result = f'Your down payment is: ${down_payment}'
print(result)
