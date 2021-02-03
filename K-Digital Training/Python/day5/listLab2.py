listnum = [10, 5, 7, 21, 4, 8, 18]
num = listnum[0]
for i in range(1,len(listnum)):
    num2 = listnum[i]
    if num > num2:
        num = num2

print('최솟값:', num)