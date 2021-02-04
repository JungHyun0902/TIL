list = [[10, 20, 30, 40, 50],
        [5, 10, 15],
        [11, 22, 33, 44],
        [9, 8, 7, 6, 5, 4, 3, 2, 13]]

def rowsum(a):
    for i in list[a-1]:
        rowsum = 0
        for j in range(len(list[a-1])):
            rowsum += list[a-1][j]
        return rowsum

for k in range(len(list)):
    print('%d행의 합은 %d 입니다.' % (k+1, rowsum(k+1)))