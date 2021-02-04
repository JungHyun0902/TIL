dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic)

print(dic['boy'])
print(dic['book'])
#print(dic['student'])
print(dic.get('student')) # get함수: 해당 key값이 없으면 None 반환
print(dic.get('student', '사전에 없는 단어')) # get함수: 해당 key값이 없으면 두번째 값(기본값) 반환

if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")

dic['boy'] = '남자애'
dic['girl'] = '소녀'
del dic['book']
print(dic)