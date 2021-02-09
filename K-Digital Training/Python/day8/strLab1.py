def myemail_info(mail):
    result = mail.split('@')
    if '@' not in mail:
        return None

    return tuple(result)

print(myemail_info('kimjh5354@gmail.com'))
print(myemail_info('kjdhf123@naver.com'))
print(myemail_info('kimjh5354gmail.com'))