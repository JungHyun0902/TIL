try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    text = f.read()
    print(text)
    text = text.lower()
    number = text.count('yesterday')
    f.close()
except FileNotFoundError:
    print('파일을 읽을 수 없어요.')
else:
    print("Number of a word 'Yesterday'"+str(number))
finally:
    print('수행완료!!')