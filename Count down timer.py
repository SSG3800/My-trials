import time

mytime = int(input('Enter Time in Seconds = '))

for x in reversed(range(0, mytime)):
    s = x % 60
    m = int(x / 60) % 60
    h = int(x / 3600)
    time.sleep(1)
    print(f'{h:02}:{m:02}:{s:02}')



print('!!!!!! Time is up !!!!!!')