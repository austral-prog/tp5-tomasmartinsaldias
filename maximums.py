def max_of_two(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x

def max_of_three(x, y, z):
    if (x>y and x>z) or (x==y and x>z) or (x>y and x==z):
        return x
    elif (y>x and y>z) or (y==x and y>z) or (y>x and y==z):
        return y
    elif (z>x and z>y) or (z==x and z>y) or (z>x and z==y):
        return z
    else: #sería el caso que x==y==z
        return x
    
#más simple
def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z