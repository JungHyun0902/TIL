import random
i = random.randint(1, 10)
j = random.randint(30, 40)
sum = 0
for k in range(i,j+1,2):
    if i % 2 == 0:
        sum += i
    else:
        sum += i+1
print("%d 부터 %d 까지의 짝수의 합 : " %(i,j), sum)

