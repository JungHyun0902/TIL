def print_gugudan(a):
    for i in range(1,10):
        print(a * i)
while True:
    num = int(input("배우고 싶은 구구단의 단수를 입력하시오.:"))
    if 1 <= num <=9:
        print_gugudan(num)
    else:
        continue
