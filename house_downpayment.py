from turtle import down


house_price = 10**6
credit = str(input("Is your credit good? If so enter 'good': "))
good = 'good'

if credit == good:
    down_payment = house_price*0.1
    msg = f'Your downpayment is ${down_payment}!'
else:
    down_payment = house_price*0.2
    msg = f'Your downpayment is ${down_payment}!'
print(msg)
