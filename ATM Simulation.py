print('-------------------')
print('WELCOME TO SSG BANK')
print('-------------------')

balance = 1000
user_pin = 1234



while True:
    input_pin = int(input('ENTER YOUR PIN : '))
    if input_pin != user_pin:
        print('Your Information is invallide')
        input()

    else:
        atm_no = True
        break





while atm_no:
    print('-----------------')
    print('WELLCOME USER')
    print('-----------------')
    print('(1) Check Balance ')
    print('(2) Deposit Money')
    print('(3) Withdraw Money')
    print('(4) Exit')
    print('------------------')

    opnum = input('Enter The Operation No. You Want : ')

    if opnum == '1':
        print('Your Balance is : $' + str(balance))

    elif opnum == '2':
        deposit = float(input('INPUT THE AMOUNT YOU WANT TO DEPOSIT : '))
        balance  += deposit
        print(f'Your ${deposit} is deposited Sucessfully  ')
        print(f'Your Avalable balance is ${balance}')

    elif opnum == '3':
        withdraw = float(input('Enter the Amount : '))
        if withdraw > balance:
            print('insufficient balance')
        else:
            balance -= withdraw
            print(f'Your ${withdraw} is Withdraw Sucessfully  ')
            print(f'Your Avalable balance is ${balance}')

    elif opnum == '4':
        break
print('--------------------------------')
print('--------------------------------')
print('Thanks For Banking With SSG Bank')
print('--------------------------------')
print('--------------------------------')



