from math import exp
import json
with open('pattern.json') as f:
    pattern = json.load(f)


def F_OR(values):
    return max(values)

def F_AND(values):
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


def one_to_lingustic(pattern_name, value, level=0.5):
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

def value_is(pattern_name, key, value, level=0.5): # because I cant use is
    v = pattern[pattern_name][key]
    return 1 if _callProperFun(v, value) >= level else 0

def add_new_pattern(pattern_name,new_pattern):
    pattern[pattern_name] = new_pattern

def get_patterns_names():
    patterns_names = []
    for k,v in pattern.items():
        patterns_names.append(k)
    return patterns_names