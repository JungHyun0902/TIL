def sumAll(*args):
    sum = 0
    num = 0
    for i in args:
        if type(i) == int:
            sum += i
            num += 1
    if len(args) == 0 or num == 0:
        sum = None
    return sum

print(sumAll(1,2,3))
print(sumAll('a','b','c'))
print(sumAll())
print(sumAll(1,2,"a"))
print(sumAll(3,4,5,"%"))

