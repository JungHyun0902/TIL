with open("sample.txt", "rt", encoding="UTF-8") as f:
    text = f.read()
print(text)

try:
    f = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")
    f.write(text)
    print('')
    print("저장이 완료되었습니다.")
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()