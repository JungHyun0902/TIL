class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def getBookInfo(self):
        return "%s\n%s\n%s\n" % (self.title, self.author, self.price)

book1 = Book('파이썬정복', '김상형', 22000)
book2 = Book('스토리텔링바이블', '대니얼 조슈아 루빈', 23000)
book3 = Book('슈독', '필 나이트', 22000 )
book4 = Book('돈의 속성', '김승호', 16800)
book5 = Book('체호프 희곡 전집', '안톤 파블로비치 체호프', 18000)
print(book1.getBookInfo())
print(book2.getBookInfo())
print(book3.getBookInfo())
print(book4.getBookInfo())
print(book5.getBookInfo())