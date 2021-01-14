# Simple Calculator

print('Simple Calculator')

ans = 'y'

while ans == 'y':
    num1 = int(input('Enter the first number:'))
    num2 = int(input('Enter the second number:'))
    ops = input('Enter what operation to be carried out(+, -, * or /):')

    a = num1 + num2
    b = num1 - num2
    c = num1 * num2
    d = num1 / num2

    if ops == '+':
        print (a)

    elif ops == '-':
        print (b)

    elif ops == '*':
        print (c)

    elif ops == '/':
        print (d)

    else:
        print ('wrong operator')
    
    ans = input('Are there any more problems?(y/n):')