import calendar
while True:
    year = input('연도를 입력하시오: ')
    month = input('해당연도의 월을 입력하시오: ')
    try:
        print('')
        year = int(year)
        month = int(month)
        print(calendar.month(year, month))
        break
    except ValueError:
        print('입력 형식이 잘못되었습니다. 숫자로 입력하세요.')
        print('')