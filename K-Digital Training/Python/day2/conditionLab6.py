import random
score = random.randint(0, 100)
if 90 <= score <= 100:
    등급 = 'A'
elif 80 <= score < 90:
    등급 = 'B'
elif 70 <= score < 80:
    등급 = 'C'
elif 60 <= score < 70:
    등급 = 'D'
else:
    등급 = 'F'
print(score, '점은', 등급, '등급입니다.')





