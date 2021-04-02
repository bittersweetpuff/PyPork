def F_OR(*values):
    return max(values)

def F_AND(*values):
    return min(values)

def F_NOT(value):
    return 1 - value
