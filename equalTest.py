import main_fuzzy as fuzzy


print("==========test 1============")
res = fuzzy.fequal(3,2,10,2)
print("result - ",res)

print("==========test 2============")
res = fuzzy.fequal(2,2,5,2)
print("result - ",res)

print("==========test 3============")
res = fuzzy.fequal(10,6,12,1)
print("result - ",res)

print("==========test 4============")
res = fuzzy.fequal(10,5,10,2)
print("result - ",res)

print("==========test 5============")
res = fuzzy.fequal(10,5,7,2)
print("result - ",res)

print("==========test 6============")
res = fuzzy.fequal(5,2,2,2)
print("result - ",res)

print("==========test 7============")
res = fuzzy.fequal(10,2,2,2)
print("result - ",res)

print("==========test 8============")
res = fuzzy.fequal(5,5,6,2)
print("result - ",res)

print("==========test 9============")
res = fuzzy.fequal(6,2,5,5)
print("result - ",res)