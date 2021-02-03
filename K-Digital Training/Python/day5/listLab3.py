listnum = [10, 5, 7, 21, 4, 8, 18]
min = listnum[0]
max = listnum[0]
for i in range(1, len(listnum)):
    num = listnum[i]
    if min > num:
        min = num
    elif max < num:
        max = num

print('최솟값:', min,',', '최댓값:', max)