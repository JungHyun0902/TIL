list = [['B', 'C', 'A', 'A'],
        ['C', 'C', 'B', 'B'],
        ['D', 'A', 'A', 'D']
        ]
count = []

def add(a):
    sum = 0
    for i in range(len(list)):
        sum += list[i].count(a)
    count.append(sum)
add('A')
add('B')
add('C')
add('D')
print('A는 %d개 입니다.' % count[0])
print('B는 %d개 입니다.' % count[1])
print('C는 %d개 입니다.' % count[2])
print('D는 %d개 입니다.' % count[3])

# for i in range(len(count)):
#    print(chr(65+i) +'는 %d개 입니다.' % count[i])