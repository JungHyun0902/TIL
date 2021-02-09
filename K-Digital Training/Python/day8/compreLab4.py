import random
numlist = []
while len(numlist) < 10:
    num = random.randint(1,100)
    if num not in numlist:
        numlist.append(num)
print(numlist)
keylist = [i for i in range(1,11)]
score = {keylist[i] :'pass' if numlist[i] >= 60 else 'nopass' for i in range(len(numlist))}
print(score)
print('')
#TODO: [다른 풀이]
print('다른 풀이')
rlist = random.sample(range(0,101),10)
print(rlist)
score = {rlist.index(i)+1: 'pass' if i >=60 else 'nopass' for i in rlist}
print(score)