listnum = []
import random
for i in range(10):
    num = random.randint(1, 50)
    listnum.append(num)
print(listnum)

for i in range(10):
    if listnum[i] < 10:
        listnum[i] = 100
print(listnum)

print(listnum[0])
print(listnum[-1])
print(listnum[1:6])
print(listnum[::-1])
print(listnum[:])
del(listnum[4])
print(listnum[:])
listnum[1:3] = []
print(listnum[:])

