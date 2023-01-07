#
# 1. La fonction sys.float_info
print(u"")
print(u"1. La fonction sys.float_info")
import sys

print(sys.float_info)
print(u"max:", sys.float_info.max)
print(u"max_exp:", TODO)
print(u"min:", TODO)
print(u"min_exp:", TODO)
print(u"mant_dig:", TODO)
print(u"epsilon:", TODO)

#
# 2. Nombre extremes
print(u"1.e1000=", 1.0e1000)
print(u"-1.e1000=", -1.0e1000)
print(u"1.e-1000=", 1.0e-1000)
print(u"-1.e-1000=", -1.0e-1000)

#
# 3. Epsilon machine
print(u"")
print(u"3. Epsilon machine")
eps = 1.0
n = 1
while 1 + eps > 1:
    eps = eps / 2.0
    print(u"n=", n, ", eps=", eps)
    n = n + 1
