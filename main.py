import fuzzy.membership_functions as fz
import matplotlib.pyplot as plt
from numpy import random

def triangle_test():
    fset = [5, 10, 12]
    values = [0, 1, 0]
    
    points = [4, 5, 8, 10, 11.6, 12, 16]
    memberships = []
    for p in points:
        memberships.append(fz.triangle_membership(p, 5, 10, 12))
    
    plt.plot(fset, values)
    plt.plot(points, memberships, 'o');
    plt.show()

def trapezoid_test():
    fset = [1, 11, 14, 15]
    values = [0, 1, 1, 0]
    
    points = [0.5, 1, 5, 11, 12.3, 14, 14.07, 15, 22]
    memberships = []
    for p in points:
        memberships.append(fz.trapezoid_membership(p, 1, 11, 14, 15))

    plt.plot(fset, values)
    plt.plot(points, memberships, 'o');
    plt.show()


def left_test():
    fset = [24, 30]
    values = [1, 0]

    points = [5, 24, 26, 30, 32]
    memberships = []
    for p in points:
        memberships.append(fz.l_class_membership(p, 24, 30))
    
    plt.plot(fset, values)
    plt.plot(points, memberships, 'o')
    plt.show()

def right_test():
    fset = [24, 30]
    values = [0, 1]

    points = [5, 24, 26, 30, 32]
    memberships = []
    for p in points:
        memberships.append(fz.y_class_membership(p, 24, 30))
    
    plt.plot(fset, values)
    plt.plot(points, memberships, 'o')
    plt.show()