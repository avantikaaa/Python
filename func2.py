def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def mul(x, y):
    return x*y
def operate(a):
    if(a=="+"):
        return add
    elif(a=="-"):
        return sub
    else:
        return mul
a = operate('+')
print a(2,3)
b = operate('-')
print b(3,2)
c = operate("*")
print c(2,3)
