import random
lotto = []
while len(lotto)<6:
    number = random.randint(1, 45)
    if number not in lotto:
        lotto.append(number)
lotto.sort()
print('행운의 로또번호:', lotto)

