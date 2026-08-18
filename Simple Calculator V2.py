num1 = float(input('First number: '))
opr = input('Operation? (+, -, *, /): ')
num2 = float(input('Second number: '))

if opr == '+':
    sol = num1 + num2
    print(num1,'+', num2,'=',sol)

elif opr == '-':
    sol = num1 - num2
    print(num1,'-', num2,'=',sol)

elif opr == '*':
    sol = num1 * num2
    print(num1,'x', num2,'=',sol)

elif opr == '/':
    if num2 == 0:
        print("Undefined")
    else:
        sol = num1 / num2
        print(num1,'÷', num2,'=',sol)

else:
  print('Operation error')