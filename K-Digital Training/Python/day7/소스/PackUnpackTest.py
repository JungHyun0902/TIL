data = [1,2,3,4]

print(data)
print(*data) # *을 list 명 앞에 붙여주면 data list의 요소값을 각각 뽑아줌
print(data[0], data[1], data[2], data[3])
'''for i in range(len(data)):
    print(data[i], end=' ')
print('')'''
print("*"*30)
a,b,c,d = [10,20,30,40]
print(a)
print(b)
print(c)
print(d)

print("*"*30)
x,*y,z = [10,20,30,40] # y앞에 *을 붙여줘서 x와 z에 대입되는 요소를 제외한 -
# 모든 요소를 y로 대입함
print(x)
print(y)
print(z)

print("*"*30)
p = 100, 200, 300
print(p)
