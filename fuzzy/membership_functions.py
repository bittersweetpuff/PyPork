from math import exp

def triangle_membership(x, a, b, c):
    if(x <= a):
        return 0
    elif(x<=b):
        return (x - a)/(b - a)
    elif(x<=c):
        return (c - x)/(c - b)
    else:
        return 0

def trapezoid_membership(x, a, b, c, d):
    if(x <= a):
        return 0
    elif(x<=b):
        return (x - a)/(b - a)
    elif(x<=c):
        return 1
    elif(x<=d):
        return (d - x)/(d - c)
    else:
        return 0

def l_class_membership(x, a, b):
    if(x <= a):
        return 1
    elif(x<=b):
        return (b-x)/(b-a)
    else:
        return 0

def y_class_membership(x, a, b):
    if(x <= a):
        return 0
    elif(x<=b):
        return (x-a)/(b-a)
    else:
        return 1

def gaussian_membership(x, mean, sd):
    #NOT WORKING (YET)
    return exp(((x - mean)**2)/2*(sd**2)) 