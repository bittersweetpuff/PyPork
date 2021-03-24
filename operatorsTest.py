import fuzzy.operators as op

values = [1, 0.5]
result_or = op.F_OR(values)
result_and = op.F_AND(values)
result_not = op.F_NOT(values[0])

print('Operators Test')
print('{0} F_OR {1} = {2}'.format(values[0], values[1], result_or))
print('{0} F_AND {1} = {2}'.format(values[0], values[1], result_and))
print('F_NOT {0} = {1}'.format(values[0], result_not))
