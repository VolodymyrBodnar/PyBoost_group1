def mult(func):
    def m(*args):
        return func(3,4)*3
    return m


@mult
def addition(x,y):
    return x + y


print(addition(0,0))