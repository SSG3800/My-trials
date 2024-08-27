while True:
         print('****************************')
         print('WELCOME SSG CALCULATOR APP')
         print('***************************')
         print('SELECT THE OPERATION YOU WANT,')
         print('1. + ')
         print('2. - ')
         print('3. * ')
         print('4. / ')


         x = input('INPUT THE OPERATION NO.= ')
         if x == '1':
            num1 = input('ENTER NUM 1 : ')
            num2 = input('ENTER NUM 2 : ')
            print('YOUR ANSWER IS :'+str(int(num1)+int(num2)))
            input()
         elif x == '2':
            num1 = input('ENTER NUM 1 : ')
            num2 = input('ENTER NUM 2 : ')
            print('YOUR ANSWER IS :' + str(int(num1) - int(num2)))
            input()
         elif x== '3':
            num1 = input('ENTER NUM 1 : ')
            num2 = input('ENTER NUM 2 : ')
            print('YOUR ANSWER IS :' + str(int(num1) * int(num2)))
            input()
         elif x=='4':
            num1 = input('ENTER NUM 1 : ')
            num2 = input('ENTER NUM 2 : ')
            print('YOUR ANSWER IS :' + str(int(num1) / int(num2)))
            input()
         else:
            print('THAT OPERATION CAN NOT DONE IN THIS CALCULATOR BECOUSE THIS IS A SIMPLE CALCULATOR YPU DUMP.')
            input()

         
