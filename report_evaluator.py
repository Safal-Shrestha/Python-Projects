# Report card evaluator

print('Report Card Evaluator')

x = 'y'
marks = ['Science', 'Maths', 'Social', 'Nepali', 'English']
print('*For total marks: 100')

while x == 'y':
    print(marks)

    a = []
    for i in list(marks):
        number = int(input("Enter {}'s marks: ".format(i)))
        a.append(number)
    
    b = a[0] + a[1] + a[2] + a[3] + a[4]
    evaluate = b / 500 * 100
    
    print(f'Marks obtained = {b} out of 500. And total percent = {evaluate}%')

    if evaluate < 40:
        print('Fail')
    elif evaluate < 50:
        print('Pass')
    elif evaluate < 60:
        print('Pass, 3rd Division')
    elif evaluate < 70:
        print('Pass, 2nd Division')
    elif evaluate < 80:
        print('Pass, 1st Division')
    elif evaluate < 100:
        print('Pass, Distinction')
    else:
        print('This student acquired beyond distinction. The student is very talented.')
    x = input('Are there anymore results to be evaluated?(y/n):')