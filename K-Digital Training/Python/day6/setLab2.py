import random
lotto = set()
while len(lotto) < 6:
    lotto.add(random.randint(1,45))

print('행운의 로또번호:',lotto)