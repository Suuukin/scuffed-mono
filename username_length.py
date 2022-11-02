name = input("Enter your name: ")
length = len(name)
valid = 'This username is valid!'
invalid = 'This username is invalid!'
if length <3:
    print(invalid)
elif length >50:
    print(invalid)
else:
    print(valid)