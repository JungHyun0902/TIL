import os

iotest = 'c:/iotest'
if not os.path.isdir(iotest):
    print('iotest디렉토리가 존재하지 않습니다.')
    os.mkdir(iotest)
    print('iotest디렉토리를 생성합니다.')
else:
    print('iotest디렉토리가 존재합니다.')

import time

now = time.localtime()
a = "오늘은 %d년 %d월 %d일입니다.\n" % (now.tm_year, now.tm_mon, now.tm_mday)
print(a)

import calendar

yoil = ['월', '화', '수', '목', '금', '토', '일']
day = calendar.weekday(2021,1,18)
birth = calendar.weekday(1989,9,2)
b = "오늘은 %s요일입니다.\n" % yoil[day]
c = '나는 %s요일에 태어났습니다.' % yoil[birth]
print(b)
print(c)

f = open("c:/iotest/today.txt", "wt")
f.write(a)
f.write(b)
f.write(c)
f.close()
print('저장이 완료되었습니다.')