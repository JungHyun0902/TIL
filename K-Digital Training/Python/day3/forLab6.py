sum = 0
for i in range(3, 51, 3):
    if i % 5 == 0:
        continue
    sum += i
print("결과 = %d" % sum)
