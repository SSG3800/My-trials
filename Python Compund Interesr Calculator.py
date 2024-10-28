# Python Compound Interest Calculator
p = 0
r = 0
t = 0

while p <= 0:
    p = float(input('Enter the principal amount ='))
    if p <= 0 :
        print('!!!!!!Your value is invalid!!!!!!')

while r <= 0:
    r = float(input('Enter the Rate ='))
    if r <= 0:
        print('!!!!!!Your value is invalid!!!!!!')

while t <= 0:
    t = float(input('Enter the Years  ='))
    if t <= 0:
        print('!!!!!!Your value is invalid!!!!!!')

final_amount= p *pow((1+ r/100), t)
print(f'Your Final Balance after {t} year/s is Rs.{final_amount:.2f}')