num1 = float(input('First number: '))
opr = input('Operation? (+, -, *, /): ')
num2 = float(input('Second number: '))

if opr == '+':
    sol = num1 + num2
    print('Solution:',sol)

elif opr == '-':
    sol = num1 - num2
    print('Solution:',sol)

elif opr == '*':
    sol = num1 * num2
    print('Solution:',sol)

elif opr == '/':
    sol = num1 / num2
    print('Solution:',sol)