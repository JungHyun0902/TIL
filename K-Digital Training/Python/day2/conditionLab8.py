import random
oper_num = random.randint(1, 10)
a = 300
b = 50
if oper_num == 1 or oper_num == 6:
    결과값 = a + b
elif oper_num == 2 or oper_num == 7:
    결과값 = a - b
elif oper_num == 3 or oper_num == 8:
    결과값 = a * b
elif oper_num == 4 or oper_num == 9:
    결과값 = a / b
else:
    결과값 = a % b
print('결과값', 결과값, sep=' : ')
