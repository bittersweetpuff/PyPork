import fuzzy.membership_functions as functions
pattern = {}

def _callProperFun(v, value):
    if v['function'] == 'triangle':
        return functions.triangle_membership(value, v['a'], v['b'], v['c'])
    elif v['function'] == 'trapezoid':
        return functions.trapezoid_membership(value, v['a'], v['b'], v['c'], v['d'])
    elif v['function'] == 'l_class':
        return functions.l_class_membership(value, v['a'], v['b'])
    elif v['function'] == 'y_class':
        return functions.y_class_membership(value, v['a'], v['b'])
    elif v['function'] == 'gaussian':
        return functions.gaussian(value, v['a'], v['b'])


def one_to_lingustic(pattern_name, value, level=0.5):
    value_patter = pattern[pattern_name]
    for k, v in value_patter.items():
        if _callProperFun(v, value) >= level:
            return k
    return "not found"

def list_to_lingustic(pattern_name, values, level=0.5):
    results = []
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

