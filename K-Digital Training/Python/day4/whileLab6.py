while True:
    number = int(input("숫자를 입력해 주세요 :"))
    if number == 0:
        print("종료")
        break
    elif number < -10 or number > 10:
        continue
    elif number > 0:
        x = 1
        for i in range(1, number+1):
            x *= i
        print("입력값:%d" % number)
        print(x)
    else:
        x = 1
        for i in range(1, (- number)+1):
            x *= i
        print("입력값(부호변경):%d" % - number)
        print(x)

