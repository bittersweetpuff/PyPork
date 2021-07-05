from math import exp
import json


def F_OR(*values):
    """
    This function does fuzzy OR operation.

    Parameters
    ----------
    values
        Numerical values which have to be tested. Each value is between 0 to 1 (both included).

    Example
    ----------
    F_OR(1, 0.5)

    F_OR(*[1, 0.5])

    Returns
    ----------
    Max value from given numerical values.
    """

    return max(values)


def F_AND(*values):
    """
    This function does fuzzy AND operation.

    Parameters
    ----------
    values
        Numerical values which have to be tested. Each value is between 0 to 1 (both included).

    Example
    ----------
    F_AND(1, 0.5)

    F_AND(*[1, 0.5])

    Returns
    ----------
    Min value from given numerical values.
    """

    return min(values)


def F_NOT(value):
    """
    This function does fuzzy NOT operation.

    Parameters
    ----------
    value
        Numerical value which has to be tested. Value is between 0 to 1 (both included).

    Example
    ----------
    F_NOT(1)

    Returns
    ----------
    Result from subtraction of one minus given numerical value.
    """

    return 1 - value


def triangle_membership(x, a, b, c):
    """
    This function represents triangular membership function.

    Parameters
    ----------
    x
        Value.
    a
        Parameter a.
    b
        Parameter b.
    c
        Parameter c.

    Example
    ----------
    triangle_membership(4, 5, 10, 12)

    Returns
    ----------
    Value between 0 to 1 (both included).
    """

    if x <= a:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    elif x <= c:
        return (c - x) / (c - b)
    else:
        return 0


def trapezoid_membership(x, a, b, c, d):
    """
    This function represents trapezoid membership function.

    Parameters
    ----------
    x
        Value.
    a
        Parameter a.
    b
        Parameter b.
    c
        Parameter c.
    d
        Parameter d.

    Example
    ----------
    trapezoid_membership(0.5, 1, 11, 14, 15)

    Returns
    ----------
    Value between 0 to 1 (both included).
    """

    if x <= a:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    elif x <= c:
        return 1
    elif x <= d:
        return (d - x) / (d - c)
    else:
        return 0


def l_class_membership(x, a, b):
    """
    This function represents L class membership function.

    Parameters
    ----------
    x
        Value.
    a
        Parameter a.
    b
        Parameter b.

    Example
    ----------
    l_class_membership(5, 24, 30)

    Returns
    ----------
    Value between 0 to 1 (both included).
    """

    if x <= a:
        return 1
    elif x <= b:
        return (b - x) / (b - a)
    else:
        return 0


def y_class_membership(x, a, b):
    """
    This function represents Y class membership function.

    Parameters
    ----------
    x
        Value.
    a
        Parameter a.
    b
        Parameter b.

    Example
    ----------
    y_class_membership(5, 24, 30)

    Returns
    ----------
    Value between 0 to 1 (both included).
    """

    if x <= a:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    else:
        return 1


def gaussian_membership(x, mean, sd):
    """
    This function represents gaussian membership function.

    Parameters
    ----------
    x
        Value.
    mean
        Parameter mean.
    sd
        Parameter sd.

    Example
    ----------
    gaussian_membership(1, 2, 5)

    Returns
    ----------
    Value between 0 to 1 (both included).
    """

    return exp(((x - mean) ** 2) / 2 * (sd ** 2))


with open('pattern.json') as f:
    pattern = json.load(f)


def _callProperFun(v, value):
    """
    This function calls appropriate membership function. It is helper function and it should not be used directly.

    Parameters
    ----------
    v
        Value of JSON object from JSON file. JSON object has to contain keys such as "function" and appropriate keys which describe parameters for given membership function. For example triangular membership function must contain "a", "b" and "c" keys.
    value
        Parameter x for membership function.

    Example
    ----------
    _callProperFun(v, value)

    Returns
    ----------
    Result from appropriate membership function. Value is between 0 to 1 (both included).
    """

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
    """
    This function converts numerical value to linguistic value.

    Parameters
    ----------
    pattern
        Linguistic value.
    value
        Numerical value which has to be converted to linguistic value.

    Example
    ----------
    one_to_lingustic('wzrost', 170)

    Returns
    ----------
    Linguistic value for given numerical value.
    """

    value_patter = pattern[pattern_name]
    max_val = 0
    max_key = ''
    for k, v in value_patter.items():
        res = _callProperFun(v, value)
        if res > max_val:
            max_val = res
            max_key = k
    return max_key


def list_to_lingustic(pattern_name, values):
    """
    This function converts numerical values to linguistic values.

    Parameters
    ----------
    pattern
        Linguistic value.
    value
        List of numerical values which have to be converted to linguistic values.

    Example
    ----------
    list_to_lingustic('wzrost', [110, 170])

    Returns
    ----------
    List of linguistic values for given numerical values.
    """

    results = []
    for value in values:
        res = one_to_lingustic(pattern_name, value)
        results.append(res)
    return results


def fuzzy_level(pattern_name, value, key):
    """
    This function does fuzzy operation.

    Parameters
    ----------
    pattern_name
        Linguistic value.
    value
        Numerical value.
    key
        Available value of linguistic value.

    Example
    ----------
    fuzzy_level('wzrost', 170, 'wysoki')

    Returns
    ----------
    Result from appropriate membership function. Value is between 0 to 1 (both included).
    """

    v = pattern[pattern_name][key]
    return _callProperFun(v, value)


def _line_intersection(L1, L2):
    """
    THIS IS PRIVATE FUNCTION USED IN FEQUAL
    This function determines if two lines intersect. It is helper function and it should not be used directly.

    Parameters
    ----------
    L1
        first line
    L2
        second line

    Example
    ----------
    _line_intersection(line1_1, line2_1)

    Returns
    ----------
    TODO
    """

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
    """
    This function does fuzzy equal operation.

    Parameters
    ----------
    value1
        First numerical value.
    value2
        Second numerical value.
    fuzzy_level1
        Fuzzy level for the first numerical value.
    fuzzy_level2
        Fuzzy level for the second numerical value.

    Example
    ----------
    run_test(3, 2, 10, 2)

    Returns
    ----------
    rate of compliance (stopień zgodności dwóch zmiennych rozmytych)
    """

    value1 = float(value1)
    value2 = float(value2)
    fuzzy_level1 = float(fuzzy_level1)
    fuzzy_level2 = float(fuzzy_level2)
    line1_1 = [[value1 - fuzzy_level1, 0.0], [value1, 1.0]]
    line1_2 = [[value1, 1.0], [value1 + fuzzy_level1, 0.0]]
    line2_1 = [[value2 - fuzzy_level2, 0.0], [value2, 1.0]]
    line2_2 = [[value2, 1.0], [value1 + fuzzy_level2, 0.0]]
    max_level = 0
    levels = [
        _line_intersection(line1_1, line2_1),
        _line_intersection(line1_1, line2_2),
        _line_intersection(line1_2, line2_1),
        _line_intersection(line1_2, line2_2)
    ]
    for lvl in levels:
        if lvl > max_level and lvl <= 1:
            max_level = lvl
    return max_level


def add_new_pattern(pattern_name, new_pattern):
    """
    This function adds new pattern. Pattern is added only to object (stored in RAM) and is not added into JSON file.

    Parameters
    ----------
    pattern
        Linguistic value which has to be added.
    value
        Dictionary which describes linguistic value.

    Example
    ----------
    add_new_pattern('wzrost', {'niski': {'function': 'triangle', 'a': 130, 'b': 155, 'c': 165},'wysoki': {'function': 'triangle', 'a': 160, 'b': 180, 'c': 190}})
    """

    pattern[pattern_name] = new_pattern


def get_patterns_names():
    """
    This function retrieves all patterns from JSON file.

    Example
    ----------
    get_patterns_names()

    Returns
    ----------
    List of patterns from JSON file.
    """

    patterns_names = []
    for k, v in pattern.items():
        patterns_names.append(k)
    return patterns_names
