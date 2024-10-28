questions = ('What is the capital of France?'
             ,'Who is the president in srilanka?'
             ,'What is the largest planet in our solar system?',
             'What is the chemical symbol for water?')
h20 = ("H\u2082O")
co2 = ("CO\u2082")
h2o2 = ("H\u2082O\u2082")
co3 = ("CO\u2083")

options = (('A. USA','B. Paris','C. Colombia','D. Tokyo'),
           ('A. dumida','B.gota','C.anura','D.ranil')
           ,('A.venus','B.jupitar','C.sun','D.earth')
           ,(f'A.{h20}',f'B.{co2}',f'C.{h2o2}',f'D.{co3}'))

answers = ('B','C','B','A')
guesses = []
score = 0
qnum = 0

for question in questions:
    print('----------------------')
    print(question)
    for option in options[qnum]:
        print(option)

    guess = input('Enter the guss (A,B,C,D) :').upper()
    guesses.append(guess)
    if guess == answers[qnum]:
        score += 1
        print('############  CORRECT  ###################')
    else:
        print('!!!!!!!!!!!!!!!!!! wrong answer !!!!!!!!!!!!!!')
        print(f'Correct answer is {answers[qnum]}')
    qnum += 1

print('=========================')
print('         RESULT          ')
print('=========================')

print(f'Number of Correct Answers :{score}')

percentage = score/len(options)*100

print(f'Your Score is : {percentage}')
if percentage >= 75:
    print("You Can Have **** A **** pass")
elif 75 >= percentage >= 50:
    print("You Can Have **** B **** pass")
elif 50 >= percentage >= 25:
    print("You Can Have **** C **** pass")
elif 25 >= percentage >= 0:
    print("You Can Have **** W **** pass")