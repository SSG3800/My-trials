credit_card_no = input('Your credit card number (ex: XXXX-XXXX-XXXX)  =')
last_digit = credit_card_no[-4:]
if len(credit_card_no) ==14:
    print(f'XXXX-XXXX-{last_digit}')
else:
    print('Your Credit Card no invalid')

