colors = {'red': '#ff0000', 'blue': '#0000ff', 'yellow': '#ffff00',
         'orange': '#ffa500', 'black': '#000000', 'white': '#ffffff',
         'violet': '#ee82ee', 'pink': '#ffc0cb', 'lime': '#00ff00' }

while True:
    color = input('칼라명을 영문으로 입력하세요 :')
    if color in colors:
        print('%s 칼라의 RGB 값은 %s 입니다.' % (color, colors[color]))
    else:
        print('%s 칼라의 RGB 값을 찾을 수 없습니다.' % color)