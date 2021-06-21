from math import exp
import json
with open('pattern.json') as f:
    pattern = json.load(f)


def F_OR(*values):
    return max(values)

def F_AND(*values):
    return min(values)

def F_NOT(value):
    return 1 - value


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
    return exp(((x - mean)**2)/2*(sd**2)) 


def _callProperFun(v, value):
    if v['function'] == 'triangle':
        return triangle_membership(value, float(v['a']), float(v['b']), float(v['c']))
    elif v['function'] == 'trapezoid':
        return trapezoid_membership(value, float(v['a']), float(v['b']), float(v['c']), float(v['d']))
    elif v['function'] == 'l_class':
        return l_class_membership(value, float(v['a']), float(v['b']))
    elif v['function'] == 'y_class':
        return y_class_membership(value, float(v['a']), float(v['b']))
    elif v['function'] == 'gaussian':
        return gaussian_membership(value, float(v['a']), float(v['b']))


def one_to_lingustic(pattern_name, value):
    value_patter = pattern[pattern_name]
    max_val = 0
    max_key = ''
    for k, v in value_patter.items():
        res = _callProperFun(v, value)
        if res > max_val :
            max_val = res
            max_key = k
    return max_key

def list_to_lingustic(pattern_name, values, level=0.5):
    results = []
    value_patter = pattern[pattern_name]
    for value in values:
        res = one_to_lingustic(pattern_name, value, level)
        results.append(res)
    return results

def fuzzy_level(pattern_name, value, key): 
    v = pattern[pattern_name][key]
    return _callProperFun(v, value)

def _line_intersection(L1,L2):
    Ax1 = L1[0][0] 
    Ay1 = L1[0][1] 
    Ax2 = L1[1][0] 
    Ay2 = L1[1][1] 
    Bx1 = L2[0][0] 
    By1 = L2[0][1]  
    Bx2 = L2[1][0] 
    By2 = L2[1][1] 
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return 0
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return 0
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    return y
def fequal(value1, fuzzy_level1, value2, fuzzy_level2): 
    value1 = float(value1)
    value2 = float(value2)
    fuzzy_level1 = float(fuzzy_level1)
    fuzzy_level2 = float(fuzzy_level2)
    line1_1 = [[value1 - fuzzy_level1,0.0], [value1,1.0]]
    line1_2 = [[value1,1.0],[value1 + fuzzy_level1,0.0]]
    line2_1 = [[value2 - fuzzy_level2,0.0], [value2,1.0]]
    line2_2 = [[value2,1.0],[value1 + fuzzy_level2,0.0]]
    max_level = 0
    levels = [
        _line_intersection(line1_1,line2_1),
        _line_intersection(line1_1,line2_2),
        _line_intersection(line1_2,line2_1),
        _line_intersection(line1_2,line2_2)
        ]
    for lvl in levels:
        if lvl > max_level and lvl <= 1:
            max_level = lvl
    return max_level

def add_new_pattern(pattern_name,new_pattern):
    pattern[pattern_name] = new_pattern

def get_patterns_names():
    patterns_names = []
    for k,v in pattern.items():
        patterns_names.append(k)
    return patterns_names
