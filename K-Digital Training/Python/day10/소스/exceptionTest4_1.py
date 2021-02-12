str = ["89", '90', '95', '53', '55', '82', '85']
try:
    for i in range(len(str)):
        score = int(str[i])
        print(score, end=' ')
    print('')
    a = str[5]
    print(a)
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")
print("작업완료")