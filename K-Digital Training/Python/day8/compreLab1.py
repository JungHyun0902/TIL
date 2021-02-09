def createList(*args, type = 1):
    if args: # 파이썬은 호출문에 나타난 실인수를 튜플로 묶어 전달. 튜플은 값이 비어있으면 거짓으로 판단.
        if type ==2: # if args는 만약 인수가 존재한다면~ 이라는 조건문을 의미함.
            result = [i for i in args if not i % 2]
        elif type ==3:
            result = [i for i in args if i % 2]
        elif type ==4:
            result = [i for i in args if i > 10]
        elif type ==1:
            result = [i for i in args]
    else:
        result = [i for i in range(1, 31)]

    return result

print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, type = 2))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, type = 3))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, type = 4))
print(createList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, type = 1))
print(createList())





