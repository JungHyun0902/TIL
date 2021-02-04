list = [[10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32],
        [34, 36, 38, 40]]
print('1행 1열의 데이터:', list[0][0])
print('3행 4열의 데이터:', list[2][3])
print('행의 개수:', len(list))
print('열의 개수:', len(list[0]))
print('3행의 데이터들:',list[2])
column_2 = [i[1] for i in list]
print('2열의 데이터들:',column_2)
ldia = []
for i in range(len(list)):
        ldia.append(list[i][i])
print('왼쪽 대각선 데이터들:', ldia)
rdia = []
for i in range(len(list)):
        rdia.append(list[i][len(list)-1-i])
print('오른쪽 대각선 데이터들:', rdia)