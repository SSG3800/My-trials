x=input('ඔයා ගේ නම මොකක්ද?')
y=int(input('ඔයා ඉපදුනේ මොන අවුරුද්දේද?'))
c=int(2024-y)
import time
if 100>c>18:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print('Hi_' + x)
    print('ඔයා හිතන්නේ ඔයා ලොකුයී කියලද!!! ලොකු නෑ හොදේ!!!')
    print('ඔයා ගෙ වයස ' + str(c))
elif c==18:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print('Hi_' + x)
    print('ඔයා ගෙ වයස ' + str(c))
    print('ලොකු උනා විතරයී හොදේ වැඩිය සද්දේ දාන්න එපා!!!')
elif 10<c<18:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print('Hi_' + x)
    print('ඔයා ගෙ වයස ' + str(c))
    print('පොඩි එකා සද්දේ වැඩී !!!!!!!!')
elif 5<c<=10:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print('Hi_' + x)
    print('ඔයා ගෙ වයස ' + str(c))
    print('මේ ළමයා Phone පාවිච්චීය වැඩී!!!!!!')
else:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print('බොරුකියන්න එපා!!!!!!!')

