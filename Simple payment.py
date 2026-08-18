A = float(input('Price item 1: '))
B = float(input('Price item 2: '))
total = A + B
print('Your total is:',total)

pay = (input('Pay with cash or card?'))

if pay == 'cash':
  print('Please insert RM:',total)

if pay == 'card':
  print('Please insert card')