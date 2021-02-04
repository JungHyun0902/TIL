import random
s1 = set()
s2 = set()

def rnum(a):
    while len(a) < 10:
        number = random.randint(1, 20)
        if number not in a:
            a.add(number)
    return a

print('집합 1:',rnum(s1))
print('집합 2:',rnum(s2))
print('두 집합에 모두 있는 데이터:', s1&s2)
print('집합1에는 있고 집합2에는 없는 데이터:',s1 - s2)
print('집합2에는 있고 집합1에는 없는 데이터:', s2 - s1)
print('집합1과 집합2가 각자 가지고 있는 데이터:', s1^s2)