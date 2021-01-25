import random
i = random.randint(5, 10)
square = 0
while square < i:
    square += 1
    print("%d -> %d" % (square, square**2))


