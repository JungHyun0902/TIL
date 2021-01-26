def print_gugudan(a):
    if type(a) == int:
        if 1 <= a <= 9:
            print("%d 단" % a)
            for i in range(1,10):
                print(a,"*",i,"=",a * i)
print_gugudan(5)
print()
print_gugudan(9)
print()
print_gugudan('*')