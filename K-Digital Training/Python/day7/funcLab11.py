def mydict(**kwargs):
    result = {}
    for kw, args in kwargs.items():
        result['my '+kw] = args
    return result

print(mydict(a=1, b=2, c=3, d =4, e=5))
print(mydict(name = 'Jude', age = 18, hobby = 'reading'))
print(mydict())