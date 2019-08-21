def customGen(x,y):
    while x< y:
        yield x
        x= x+1


r = customGen(20,30)
print r;
for i in r: print i
