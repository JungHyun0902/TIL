def sumEven1(*args):
    sum = 0
    for i in args:
        if i >= 1:
            if i % 2 == 0:
                sum += i
    if len(args) == 0:
        sum = -1
    return sum

print(sumEven1(1,2,3,4,5,6))
print(sumEven1())
print(sumEven1(1,3,5,7))
