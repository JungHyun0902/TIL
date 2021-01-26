def print_triangle(a):
    for i in range(a,0,-1):
        for j in range(i):
            print('@', end="")
        print('')

while True:
    num = int(input("숫자를 입력하시오. :"))
    if 1 <= num <= 10:
        print_triangle(num)
    else:
        continue