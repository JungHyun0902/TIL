evenNum = 0
oddNum = 0
for i in range(1,101,2):
    evenNum += i
for j in range(2,101,2):
    oddNum += j
result = '''
1부터 100까지의 숫자들 중에서
짝수의 합은 %d 이고
홀수의 합은 %d 이다
'''
print(result %(evenNum, oddNum))