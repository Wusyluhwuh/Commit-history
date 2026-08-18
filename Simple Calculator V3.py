def Calc():

    try:
      num1 = float(input('First number: '))
    except:
      print('Invalid number')
      return
      
    opr = input('Operation? (+,-, *, /): ')
    if opr not in ['+','-','*','/']:
      print('Invalid operator')
      return
    
    try:
      num2 = float(input('Second number: '))
    except:
      print('invalid number')
      return
    
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

Calc()