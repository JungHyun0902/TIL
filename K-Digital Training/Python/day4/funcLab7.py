def differtwovalue(a, b):
    if a > b:
        result = a - b
    elif a < b:
        result = b - a
    else:
        result = 0
    return result

import random
rep = 0
while rep < 5:
    rep += 1
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    print("%d와 %d의 차이는 %d이 입니다." %(a, b, differtwovalue(a, b)))