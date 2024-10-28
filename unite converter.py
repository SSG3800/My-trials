# Unit Converter
unit = input('Enter The Unit of the temp Fahrenheit or Celsius (C/F) = ')
temp = float(input('Enter the temp = '))


if unit == 'C':
   temp = round((9 * temp) / 5 + 32, 1)
   print(f'The Temperature in Fahrenheit is : {temp}°F ')
elif unit == 'F' :
   temp = round((temp - 32) * 5 / 9, 1)
   print(f'The Temperature in Celsius is : {temp} °C ')
else:
   print(f'The Unit {temp} is not valid.')
