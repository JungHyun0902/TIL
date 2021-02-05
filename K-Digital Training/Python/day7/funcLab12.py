def myprint(*args, **kwargs):
    args = 'Hello Python'
    deco = '**'
    sep = ','
    if 'deco' in kwargs.keys():
        deco = kwargs['deco']
    if 'sep' in kwargs.keys():
        sep = kwargs['sep']
    print(deco+args+deco,sep= sep)


myprint(10,20,30,deco='@',sep='-')
myprint("python","javascript","R",deco="$")
myprint("가,""나","다")
myprint(100)
myprint(True,111,False,"abc",deco="&",sep="")
