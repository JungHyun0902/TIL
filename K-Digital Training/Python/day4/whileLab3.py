import random
count = -1
while True:
    count += 1
    i = random.randint(0, 30)
    if 0 < i < 27:
        print(chr(i + 64)+"(%d)" % i)
    else:
        print("수행횟수는 %d 번입니다." % count)
        break


