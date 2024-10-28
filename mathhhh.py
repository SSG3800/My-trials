#area of a circle
import math

base = float(input('enter base ='))
height = float(input('enter height ='))
x = pow(base, 2)
y = pow(height, 2)
hypo = math.sqrt(x+y)
print(hypo)