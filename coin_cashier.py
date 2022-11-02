import math
cents = int(input('How many cents do you have?'))
quarter = 25
dime = 10
nickel = 5
quarters = cents/quarter
remainder = cents%quarter
dimes = remainder/dime
remainder1 = remainder%dime
nickels = remainder1/nickel
remainder2 = remainder1%nickel
pennies = remainder2
print(math.floor(int(quarters)))
print(math.floor(int(dimes)))
print(math.floor(int(nickels)))
print(pennies)
# print(remainder)
# print(remainder1)
# print(remainder2)