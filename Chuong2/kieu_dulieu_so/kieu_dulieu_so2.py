# phần phía sau dấu chấm có độ xấp xỉ 15 chữ số thập phân (tức là chỉ lấy đúng 15 số, và làm tròn)
a = 1.123456789101112131415
print(a)
print(type(a))

# lấy toàn bộ nội dung của thư viện decimal
from decimal import*

# lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec = 30

# chỉ lấy đúng 15 phần thập phân
s = 10/3
print(s)
print(type(s))

# lấy đúng 30 phần thập phân
f = Decimal(10)/3
print(f)
print(type(f))
