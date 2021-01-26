def print_triangle(a):
    for i in range(1, a+1):
        print('*' * i)

while True:
    num = int(input("숫자를 입력하시오. :"))
    if 1 <= num <= 10:
        print_triangle(num)
    else:
        continue