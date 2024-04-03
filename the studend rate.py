number = float(input('Enter the student mark \n'))
if number >= 90:
  print('Excellent')
elif number < 90 and number >= 75:
  print('good')
elif number < 75 and number >= 50:
  print('acceptable')
else:
    print('weak')
  