class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)

    def getBookInfo(self):
        print(self.title)
        print(self.author)
        print(str(self.price))
        print('-'*10)

book1 = Book('파이썬정복', '김상형', 22000)
book2 = Book('스토리텔링바이블', '대니얼 조슈아 루빈', 23000)
book3 = Book('슈독', '필 나이트', 22000 )
book4 = Book('돈의 속성', '김승호', 16800)
book5 = Book('체호프 희곡 전집', '안톤 파블로비치 체호프', 18000)
book1.getBookInfo()
book2.getBookInfo()
book3.getBookInfo()
book4.getBookInfo()
book5.getBookInfo()