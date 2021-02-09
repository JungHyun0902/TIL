def mycompredict(**kwargs):
    dic = {'my '+kw : args for kw, args in kwargs.items()}
    return dic

print(mycompredict(korean = 95, math = 93, english = 92))
print(mycompredict())