while True:
    month = int(input("좋아하는 달(월)에 해당하는 숫자를 입력하세요."))
    if month in [12, 1, 2]:
        print("%d월은 겨울" % month)
    elif month in [3, 4, 5]:
        print("%d월은 봄" % month)
    elif month in [6, 7, 8]:
        print("%d월은 여름" % month)
    elif month in [9, 10, 11]:
        print("%d월은 가을" % month)
    else:
        break
print("1~12 사이의 값을 입력하세요!")
