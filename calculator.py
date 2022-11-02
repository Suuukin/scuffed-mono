a = float(input('What is your first number? a = '))
b = float(input('What is your second number? b = '))
op = input('What is the operator you would like to use (*,/,+,-)? ')

if op == '*':
    p = a * b
elif op == '/':
    if b == 0:
        print('Math error: Cannot divide by 0')
    else:
        p = a / b
elif op == '+':
    p = a + b
elif op == '-':
    p = a - b
if p.is_integer():
    p = int(p)
if a.is_integer():
    a = int(a)
if b.is_integer():
    b = int(b)
else:
    print('Did not recognize as operator.')
    
print(f'{a} {op} {b} = {p}')